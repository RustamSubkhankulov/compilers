#include <iostream>
#include "lexer.hpp"

using namespace Lexer;

#ifdef DUMP_JSON
static void dump_tokens(const std::vector<std::unique_ptr<Token>>& tokens) {

  std::cout << "{\"tokens\":[";

  for (unsigned long ind = 0; ind < tokens.size(); ++ind) {
    
    std::cout << *tokens[ind];
    if (ind != tokens.size() - 1) {
      std::cout << ',';
    }
  }

  std::cout << "]}";
  
  return;
}
#endif

int main() {

  auto& tokens = get_tokens();

#ifdef DUMP_JSON
  dump_tokens(tokens);
#endif

  return 0;
}