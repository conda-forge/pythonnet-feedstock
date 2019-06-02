cert-sync --user $PREFIX/ssl/cacert.pem

PY_LIBDIR=$($PYTHON -c 'import sysconfig; print(sysconfig.get_config_var("LIBDIR"))')
export LD_LIBRARY_PATH=$PY_LIBDIR:$BUILD_PREFIX/x86_64-conda_cos6-linux-gnu/sysroot/usr/lib/:$LD_LIBRARY_PATH

$PYTHON -m pip install . -vv
