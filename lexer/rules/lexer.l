/* Options. */
%option noyywrap nounput noinput

/* Includes. */
%top {
  #include <iostream>
  #include <vector>
  #include <memory>
  #include "lexer.hpp"
}

/* Definitions. */
%{
using namespace Lexer;
std::vector<std::unique_ptr<Token>> tokens_parsed;
%}

/* Categories. */

DIGIT0  [0-9]
DIGIT1  [1-9]
ALPHA   [A-z]|[a-z]

DECINT  {DIGIT0}|({DIGIT1}{DIGIT0}*)
NUMINT  [-+]?{DECINT}

DECFLT  ({DECINT}?[.]{DIGIT0}{0,6})|({DECINT}[.]({DIGIT0}{0,6})?)
NUMFLT  [-+]?{DECFLT}

NAME    {ALPHA}({ALPHA}|{DECINT})*
ID      ((\$|NAME)_)?NAME

/* Rules section. */
%%

{NUMINT}      {
                tokens_parsed.push_back(std::make_unique<Token_num<int>>(std::stoi(yytext))); 
              }

{NUMFLT}      {
                tokens_parsed.push_back(std::make_unique<Token_num<float>>(std::stof(yytext))); 
              }

{NAME}        {
                tokens_parsed.push_back(std::make_unique<Token_var_id>(yytext));
              }

[[:space:]]+  // skip whitespace

[[:^space:]]+ { 
                std::cerr << "ERROR: " << yytext << std::endl;
                exit(EXIT_FAILURE); 
              }

%%

/* Code section. */

int main() {

  yylex();
  
  std::cout << std::endl;

  for (const auto& token_ptr : tokens_parsed) {
    std::cout << *token_ptr << std::endl;
  }

  return 0;
}
