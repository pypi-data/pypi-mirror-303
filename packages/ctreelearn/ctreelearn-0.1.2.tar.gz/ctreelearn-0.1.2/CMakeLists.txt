# Instruções de compilação
#
# Compilar somente os arquivos de teste: 
#    cmake -DBUILD_PYBIND=OFF -DBUILD_DEBUG=ON -DBUILD_TESTS=ON -DCMAKE_PREFIX_PATH=$(python -c "import torch; print(torch.utils.cmake_prefix_path);") ../
#    cmake -DBUILD_PYBIND=OFF -DBUILD_DEBUG=OFF -DBUILD_TESTS=ON -DCMAKE_PREFIX_PATH=$(python -c "import torch; print(torch.utils.cmake_prefix_path);") ../
#
# Compilar o modulo Python:
#    cmake -DPYTHON_LIBRARY_DIR=$(python -c "import sysconfig; print(sysconfig.get_config_var('LIBDIR'))") -DPYTHON_EXECUTABLE=$(python -c "import sys; print(sys.executable)") -DCMAKE_PREFIX_PATH=$(python -c "import torch; print(torch.utils.cmake_prefix_path);") ../
#
# Depois:
#   make
#   make install

cmake_minimum_required(VERSION 3.14)
project(ctreelearn)

# Opções configuráveis
option(BUILD_PYBIND "Enable building Python bindings with pybind11" ON)
option(BUILD_DEBUG "Enable Debug mode" OFF)
option(BUILD_TESTS "Enable building of tests" OFF)

# Configurações de compilação (Release por padrão)
if(BUILD_DEBUG)
    set(CMAKE_BUILD_TYPE Debug)
    set(CMAKE_CXX_FLAGS_DEBUG "-g -O0")
else()
    set(CMAKE_BUILD_TYPE Release)
    set(CMAKE_CXX_FLAGS "-O3")
    set(CMAKE_CXX_FLAGS_RELEASE "-O3")
endif()

# Padrões de C++
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Incluir pybind11 se BUILD_PYBIND estiver ativado
if(BUILD_PYBIND)
    
    include(FetchContent)
    FetchContent_Declare(
        pybind11
        GIT_REPOSITORY https://github.com/pybind/pybind11.git
        GIT_TAG v2.10.4
    )
    FetchContent_MakeAvailable(pybind11)

    file (GLOB SOURCE_FILES "ctreelearn/src/*.cpp")
    file (GLOB HEADER_FILES "ctreelearn/include/*.hpp" "ctreelearn/pybind/*.hpp")

    # Set up such that XCode organizes the files
    source_group(TREE ${CMAKE_CURRENT_SOURCE_DIR} FILES ${SOURCE_FILES} ${HEADER_FILES} )

    # Arquivo fonte principal do módulo pybind
    set(PYBIND_CPP_FILE "ctreelearn/ctreelearn.cpp")
    
    pybind11_add_module(ctreelearn ${PYBIND_CPP_FILE}
      ${SOURCE_FILES}
      ${HEADER_FILES}
    )

    find_package(Torch REQUIRED)
    find_library(TORCH_PYTHON_LIBRARY torch_python PATH "${TORCH_INSTALL_PREFIX}/lib")
    target_link_libraries(ctreelearn PUBLIC "${TORCH_LIBRARIES}" "${TORCH_PYTHON_LIBRARY}")
    install(TARGETS ctreelearn
      COMPONENT python
      LIBRARY DESTINATION "${PYTHON_LIBRARY_DIR}"
      )

endif()

# Condicionalmente adicionar a compilação de testes
if(BUILD_TESTS)
    #crei uma lib ctreelearn_lib
    add_subdirectory(ctreelearn)

    # Adicionar o executável de testes
    add_executable(testeResidualTree 
        ctreelearn/test/testeResidualTree.cpp
    )
    target_link_libraries(testeResidualTree PRIVATE ctreelearn_lib)

    find_package(Torch REQUIRED)

    # Adicionar teste com PyTorch
    add_executable(testeTensor
        ctreelearn/test/testeTensor.cpp
    )
    target_link_libraries(testeTensor PRIVATE ctreelearn_lib "${TORCH_LIBRARIES}")

endif()
