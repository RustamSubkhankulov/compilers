cmake_minimum_required(VERSION 3.21)

project(
        lexer
        DESCRIPTION "Lexical scanner for Yazik++"
        LANGUAGES CXX
        )

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_CXX_EXTENSIONS False)

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
  message(STATUS "CMAKE_BUILD_TYPE is not specified, using Release by default")
endif()

set(CMAKE_CXX_FLAGS "-Wall -Wextra")
set(CMAKE_CXX_FLAGS_DEBUG "-g")
set(CMAKE_CXX_FLAGS_RELEASE "-O2")

set(SRC_DIR src)
set(INC_DIR inc)

find_package(FLEX REQUIRED)
FLEX_TARGET(lexer ${CMAKE_SOURCE_DIR}/rules/lexer.l ${CMAKE_CURRENT_BINARY_DIR}/lexer.cpp)

file(GLOB SOURCES CONFIGURE_DEPENDS ${SRC_DIR}/*.cpp)

include_directories(${CMAKE_CURRENT_BINARY_DIR})
add_executable(${PROJECT_NAME} 
  ${SOURCES}
  ${FLEX_lexer_OUTPUTS}
  )

target_include_directories(${PROJECT_NAME} PRIVATE ${INC_DIR})
