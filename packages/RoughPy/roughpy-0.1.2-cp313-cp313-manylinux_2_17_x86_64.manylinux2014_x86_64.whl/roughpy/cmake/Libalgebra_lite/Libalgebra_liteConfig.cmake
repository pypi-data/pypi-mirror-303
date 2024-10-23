

####### Expanded from @PACKAGE_INIT@ by configure_package_config_file() #######
####### Any changes to this file will be overwritten by the next CMake run ####
####### The input file was Libalgebra_liteConfig.cmake.in                            ########

get_filename_component(PACKAGE_PREFIX_DIR "${CMAKE_CURRENT_LIST_DIR}/../../../" ABSOLUTE)

macro(set_and_check _var _file)
  set(${_var} "${_file}")
  if(NOT EXISTS "${_file}")
    message(FATAL_ERROR "File or directory ${_file} referenced by variable ${_var} does not exist !")
  endif()
endmacro()

macro(check_required_components _NAME)
  foreach(comp ${${_NAME}_FIND_COMPONENTS})
    if(NOT ${_NAME}_${comp}_FOUND)
      if(${_NAME}_FIND_REQUIRED_${comp})
        set(${_NAME}_FOUND FALSE)
      endif()
    endif()
  endforeach()
endmacro()

####################################################################################


list(APPEND CMAKE_MODULE_PATH "${PACKAGE_PREFIX_DIR}/cmake")

if (CMAKE_VERSION VERSION_LESS 3.19)
    set(${CMAKE_FIND_PACKAGE_NAME}_NOT_FOUND_MESSAGE
            "Libalgebra_lite requires CMake 3.19 or later")
    set(${CMAKE_FIND_PACKAGE_NAME}_FOUND FALSE)
    return()
endif()
cmake_minimum_required(VERSION 3.19)


include(CMakeFindDependencyMacro)
find_dependency(Boost REQUIRED)

if (OFF)
    list(PREPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/Modules")
    find_dependency(Bignum REQUIRED)
endif()


include(${CMAKE_CURRENT_LIST_DIR}/Libalgebra_liteTargets.cmake)
