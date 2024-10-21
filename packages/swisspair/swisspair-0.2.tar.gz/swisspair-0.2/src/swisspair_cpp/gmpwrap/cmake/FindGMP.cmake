# Try to find the GNU Multiple Precision Arithmetic Library (GMP)
# See http://gmplib.org/
# Taken from https://github.com/libigl/eigen/blob/master/cmake/FindGMP.cmake

find_path(GMP_INCLUDES
  NAMES
  gmp.h
  PATHS
  $ENV{GMPDIR}
  ${INCLUDE_INSTALL_DIR}
)

find_library(GMP_LIBRARIES gmp PATHS $ENV{GMPDIR} ${LIB_INSTALL_DIR})

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(GMP DEFAULT_MSG
                                  GMP_INCLUDES GMP_LIBRARIES)
mark_as_advanced(GMP_INCLUDES GMP_LIBRARIES)
