extern crate parol_runtime;

mod modelica_grammar;

mod dae;
mod ir;
mod modelica_grammar_trait;
mod modelica_parser;
mod visitor;
use indexmap::IndexMap;
use minijinja::{Environment, context};
use visitor::Visitor;

use crate::modelica_grammar::ModelicaGrammar;
use crate::modelica_parser::parse;
use anyhow::{Context, Result};

use parol_runtime::{Report, log::debug};
use std::{fs, time::Instant};

use clap::Parser;

#[derive(Parser, Debug)]
#[command(version, about = "Rumoca Modelica Translator", long_about = None)]
struct Args {
    /// Template file to render to
    #[arg(short, long)]
    template_file: Option<String>,

    /// Modelica file to parse
    #[arg(name = "MODELICA_FILE")]
    model_file: String,

    /// Verbose output
    #[arg(short, long, default_value_t = false)]
    verbose: bool,
}

pub fn panic(msg: &str) {
    panic!("{:?}", msg);
}

pub fn warn(msg: &str) {
    eprintln!("{:?}", msg);
}

struct ErrorReporter;
impl Report for ErrorReporter {}

fn main() -> Result<()> {
    env_logger::init();
    debug!("env logger started");
    let args = Args::parse();

    let file_name = args.model_file.clone();
    let input = fs::read_to_string(file_name.clone())
        .with_context(|| format!("Can't read file {}", file_name))?;

    let mut modelica_grammar = ModelicaGrammar::new();
    let now = Instant::now();
    match parse(&input, &file_name, &mut modelica_grammar) {
        Ok(_syntax_tree) => {
            let elapsed_time = now.elapsed();

            // parse
            let mut def = modelica_grammar.modelica.expect("failed to parse");
            if args.verbose {
                println!("Parsing took {} milliseconds.", elapsed_time.as_millis());
                println!("Success!\n{:#?}", def);
            }

            // flatten the syntax tree
            let mut count = 0;
            let mut main_class_name = String::new();
            let mut class_dict = IndexMap::new();

            for (class_name, class) in &def.class_list {
                if count == 0 {
                    main_class_name = class.name.text.clone();
                } else {
                    class_dict.insert(class_name.clone(), class.clone());
                }
                count += 1;
            }

            let mut flat_class = None;

            if let Some(main_class) = def.class_list.get(&main_class_name) {
                // create flat class
                let mut fclass = main_class.clone();

                // for each component in the main class
                for (comp_name, comp) in &main_class.components {
                    // if the the component type is a class
                    if class_dict.contains_key(&comp.type_name.to_string()) {
                        let comp_class = class_dict.get(&comp.type_name.to_string()).unwrap();

                        // add equaition from component to flat class
                        for eq in &comp_class.equations {
                            fclass.equations.push(eq.clone());
                        }

                        fclass.accept(&mut visitor::sub_comp_namer::SubCompNamer {
                            comp: comp_name.clone(),
                        });

                        // add subcomponents from component to flat class
                        for (subcomp_name, subcomp) in &comp_class.components {
                            let mut scomp = subcomp.clone();
                            let name = format!("{}_{}", comp_name, subcomp_name);
                            scomp.name = name.clone();
                            fclass.components.insert(name, scomp);
                        }

                        // remove compoment from flat class, as it has been expanded
                        fclass.components.swap_remove(comp_name);
                    }
                }
                flat_class = Some(fclass);
            }

            if let Some(mut fclass) = flat_class {
                println!("Flat Class: {:#?}", fclass);
            }

            // render template
            if args.template_file.is_some() {
                if let Some(template_file) = &args.template_file {
                    let template_txt = fs::read_to_string(template_file)
                        .with_context(|| format!("Can't read file {}", template_file))?;

                    let mut env = Environment::new();
                    env.add_function("panic", panic);
                    env.add_function("warn", warn);
                    env.add_template("template", &template_txt)?;
                    let tmpl = env.get_template("template")?;
                    let txt = tmpl.render(context!(def => def)).unwrap();
                    println!("{}", txt);
                }
            }
            Ok(())
        }
        Err(e) => ErrorReporter::report_error(&e, file_name),
    }
}
