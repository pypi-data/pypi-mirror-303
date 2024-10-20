mod completions;
mod config;
mod lang;
mod lsp;
mod new;
mod print;
mod run;
mod scan;
mod utils;
mod verify;

use anyhow::Result;
use clap::{Parser, Subcommand};

use completions::{run_shell_completion, CompletionsArg};
use lsp::{run_language_server, LspArg};
use new::{run_create_new, NewArg};
use run::{register_custom_language_if_is_run, run_with_pattern, RunArg};
use scan::{run_with_config, ScanArg};
use utils::exit_with_error;
use verify::{run_test_rule, TestArg};

const LOGO: &str = r#"
Search and Rewrite code at large scale using AST pattern.
                    __
        ____ ______/ /_      ____ _________  ____
       / __ `/ ___/ __/_____/ __ `/ ___/ _ \/ __ \
      / /_/ (__  ) /_/_____/ /_/ / /  /  __/ /_/ /
      \__,_/____/\__/      \__, /_/   \___/ .___/
                          /____/         /_/
"#;
#[derive(Parser)]
#[clap(author, version, about, long_about = LOGO)]
/**
 * TODO: add some description for ast-grep: sg
 * Example:
 * sg -p "$PATTERN.to($MATCH)" -l ts --rewrite "use($MATCH)"
 */
struct App {
  #[clap(subcommand)]
  command: Commands,
}

#[derive(Subcommand)]
enum Commands {
  /// Run one time search or rewrite in command line. (default command)
  Run(RunArg),
  /// Scan and rewrite code by configuration.
  Scan(ScanArg),
  /// Test ast-grep rules.
  Test(TestArg),
  /// Create new ast-grep project or items like rules/tests.
  New(NewArg),
  /// Start language server.
  Lsp(LspArg),
  /// Generate shell completion script.
  Completions(CompletionsArg),
  /// Generate rule docs for current configuration. (Not Implemented Yet)
  Docs,
}

pub fn execute_main() -> Result<()> {
  match main_with_args(std::env::args()) {
    Err(error) => exit_with_error(error),
    ok => ok,
  }
}

fn try_default_run(args: &[String]) -> Result<Option<RunArg>> {
  // use `run` if there is at lease one pattern arg with no user provided command
  let should_use_default_run_command =
    args.iter().skip(1).any(|p| p == "-p" || p == "--pattern") && args[1].starts_with('-');
  if should_use_default_run_command {
    // handle no subcommand
    let arg = RunArg::try_parse_from(args)?;
    Ok(Some(arg))
  } else {
    Ok(None)
  }
}

// this wrapper function is for testing
pub fn main_with_args(args: impl Iterator<Item = String>) -> Result<()> {
  let args: Vec<_> = args.collect();
  register_custom_language_if_is_run(&args)?;
  if let Some(arg) = try_default_run(&args)? {
    return run_with_pattern(arg);
  }

  let app = App::try_parse_from(args)?;
  // TODO: add test for app parse
  match app.command {
    Commands::Run(arg) => run_with_pattern(arg),
    Commands::Scan(arg) => run_with_config(arg),
    Commands::Test(arg) => run_test_rule(arg),
    Commands::New(arg) => run_create_new(arg),
    Commands::Lsp(arg) => run_language_server(arg),
    Commands::Completions(arg) => run_shell_completion::<App>(arg),
    Commands::Docs => todo!("todo, generate rule docs based on current config"),
  }
}

#[cfg(test)]
mod test_cli {
  use super::*;

  fn sg(args: &str) -> Result<App> {
    let app = App::try_parse_from(
      std::iter::once("sg".into()).chain(args.split(' ').map(|s| s.to_string())),
    )?;
    Ok(app)
  }

  fn ok(args: &str) -> App {
    sg(args).expect("should parse")
  }
  fn error(args: &str) -> clap::Error {
    let Err(err) = sg(args) else {
      panic!("app parsing should fail!")
    };
    err
      .downcast::<clap::Error>()
      .expect("should have clap::Error")
  }

  #[test]
  fn test_wrong_usage() {
    error("");
    error("Some($A) -l rs");
    error("-l rs");
  }

  #[test]
  fn test_version_and_help() {
    let version = error("--version");
    assert!(version.to_string().starts_with("ast-grep"));
    let version = error("-V");
    assert!(version.to_string().starts_with("ast-grep"));
    let help = error("--help");
    assert!(help.to_string().contains("Search and Rewrite code"));
  }

  fn default_run(args: &str) {
    let args: Vec<_> = std::iter::once("sg".into())
      .chain(args.split(' ').map(|s| s.to_string()))
      .collect();
    assert!(matches!(try_default_run(&args), Ok(Some(_))));
  }
  #[test]
  fn test_no_arg_run() {
    let ret = main_with_args(["sg".to_owned()].into_iter());
    let err = ret.unwrap_err();
    assert!(err.to_string().contains("sg <COMMAND>"));
  }
  #[test]
  fn test_default_subcommand() {
    default_run("-p Some($A) -l rs");
    default_run("-p Some($A)");
    default_run("-p Some($A) -l rs -r $A.unwrap()");
  }

  #[test]
  fn test_run() {
    ok("run -p test -i");
    ok("run -p test --interactive dir");
    ok("run -p test -r Test dir");
    ok("run -p test -l rs --debug-query");
    ok("run -p test -l rs --debug-query not");
    ok("run -p test -l rs --debug-query=ast");
    ok("run -p test -l rs --debug-query=cst");
    ok("run -p test -l rs --color always");
    ok("run -p test -l rs --heading always");
    ok("run -p test dir1 dir2 dir3"); // multiple paths
    ok("run -p testm -r restm -U"); // update all
    ok("run -p testm -r restm --update-all"); // update all
    ok("run -p test --json compact"); // argument after --json should not be parsed as JsonStyle
    ok("run -p test --json=pretty dir");
    ok("run -p test --json dir"); // arg after --json should not be parsed as JsonStyle
    ok("run -p test --strictness ast");
    ok("run -p test --strictness relaxed");
    ok("run -p test --selector identifier"); // pattern + selector
    ok("run -p test --selector identifier -l js");
    ok("run -p test --follow");
    ok("run -p test --globs '*.js'");
    ok("run -p test --globs '*.{js, ts}'");
    ok("run -p test --globs '*.js' --globs '*.ts'");
    ok("run -p fubuki -j8");
    ok("run -p test --threads 12");
    error("run test");
    error("run --debug-query test"); // missing lang
    error("run -r Test dir");
    error("run -p test -i --json dir"); // conflict
    error("run -p test -l rs -c always"); // no color shortcut
    error("run -p test -U");
    error("run -p test --update-all");
    error("run -p test --strictness not");
    error("run -p test -l rs --debug-query=not");
    error("run -p test --selector");
    error("run -p test --threads");
  }

  #[test]
  fn test_scan() {
    ok("scan");
    ok("scan dir");
    ok("scan -r test-rule.yml dir");
    ok("scan -c test-rule.yml dir");
    ok("scan -c test-rule.yml");
    ok("scan --report-style short"); // conflict
    ok("scan dir1 dir2 dir3"); // multiple paths
    ok("scan -r test.yml --format github");
    ok("scan --format github");
    ok("scan --interactive");
    ok("scan --follow");
    ok("scan -r test.yml -c test.yml --json dir"); // allow registering custom lang
    ok("scan --globs '*.js'");
    ok("scan --globs '*.{js, ts}'");
    ok("scan --globs '*.js' --globs '*.ts'");
    ok("scan -j 12");
    ok("scan --threads 12");
    error("scan -i --json dir"); // conflict
    error("scan --report-style rich --json dir"); // conflict
    error("scan -r test.yml --inline-rules '{}'"); // conflict
    error("scan --format gitlab");
    error("scan --format github -i");
    error("scan --format local");
    error("scan --json=dir"); // wrong json flag
    error("scan --json= not-pretty"); // wrong json flag
    error("scan -j");
    error("scan --threads");
  }

  #[test]
  fn test_test() {
    ok("test");
    ok("test -c sgconfig.yml");
    ok("test --skip-snapshot-tests");
    ok("test -U");
    ok("test --update-all");
    error("test --update-all --skip-snapshot-tests");
  }

  #[test]
  fn test_shell() {
    ok("completions");
    ok("completions zsh");
    ok("completions fish");
    error("completions not-shell");
    error("completions --shell fish");
  }
}
