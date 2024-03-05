#include <iostream>

#include "lexer.hpp"

using namespace Lexer;
extern std::vector<std::unique_ptr<Token>> Tokens_parsed;

void dump_tokens() {

  std::cout << "{\"tokens\":[";

  for (unsigned long ind = 0; ind < Tokens_parsed.size(); ++ind) {
    
    std::cout << *Tokens_parsed[ind];
    if (ind != Tokens_parsed.size() - 1) {
      std::cout << ',';
    }
  }

  std::cout << "]}";
  
  return;
}