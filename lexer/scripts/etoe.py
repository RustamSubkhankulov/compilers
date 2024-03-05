#!/usr/bin/python3

import json
import sys
from subprocess import Popen, PIPE, STDOUT

#===============

def run_test(cmnd: str, input_string: str):
  """
  Run tested lexer and get its output.
  """
  p = Popen(cmnd, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
  stdout = p.communicate(input=input_string.encode())[0]
  return stdout.decode()

def load_test_data(test_data_filename: str):
  """
  Load json from data file.
  """
  with open(test_data_filename) as test_data_file:
    return json.loads(test_data_file.read())

def prepare_input(jdata) -> str:
  """
  Parse json and form an input string for lexer.
  """
  input_string = ""

  for entry in jdata["test_data"]:
    input_string = input_string + entry["token"] + " "

  return input_string

#===============
# MAIN
#===============

if len(sys.argv) != 3:
  print("Usage: ./etoe.py executable data.json\n")
  sys.exit(1)

# Parse args
cmnd = sys.argv[1]
test_data_filename = sys.argv[2]

# Load data in json format from file. 
jdata = load_test_data(test_data_filename)

# Prepare input string for lexer.
input_string = prepare_input(jdata)

# Run test and get output as json.
lexer_output = json.loads(run_test(cmnd, input_string))

failed = False

# Check lexer work.
for ind in range(len(lexer_output["tokens"])):

  test_entry = jdata["test_data"][ind] 
  res_entry  = lexer_output["tokens"][ind]

  if test_entry["class"] != res_entry["class"]:
    print("Invalid token class:")
    print(f"Token: {test_entry['token']} Expected class: {test_entry['class']}")
    print(f"Got class: {res_entry['class']}")

  if "value" in test_entry.items():
    if test_entry["value"] != res_entry["value"]:
      print("Invalid token value:")
      print(f"Token: {test_entry['token']} Expected value: {test_entry['value']}")
      print(f"Got value: {res_entry['value']}")

if not failed:
  print("All tests passed successfully ^_^")