//! A `ScopePusher` is a visitor that modifies component references in an abstract syntax tree (AST).
//!
//! # Fields
//! - `comp`: A `String` representing the component name to be prepended to certain component references.
//!
//! # Behavior
//! This visitor implements the `Visitor` trait and overrides the `exit_component_reference` method.
//! When visiting a `ComponentReference` node, it checks if the first part of the reference's identifier
//! is not `"der"`. If this condition is met, it prepends a new `ComponentRefPart` to the reference's parts,
//! using the `comp` field as the identifier text.
//!
//! This is useful for ensuring that component references are properly scoped by adding a prefix
//! to their identifiers when necessary.
use crate::ir;
use crate::ir::visitor::Visitor;

#[derive(Debug, Default, Clone, PartialEq)]
pub struct ScopePusher {
    pub comp: String,
}

impl Visitor for ScopePusher {
    fn exit_component_reference(&mut self, node: &mut ir::ast::ComponentReference) {
        if node.parts[0].ident.text != "der" {
            node.parts.insert(
                0,
                ir::ast::ComponentRefPart {
                    ident: ir::ast::Token {
                        text: self.comp.clone(),
                        ..Default::default()
                    },
                    subs: None,
                },
            );
        }
    }
}
