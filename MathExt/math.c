#include "Python.h"
#include <stdlib.h>

uint32_t square(uint32_t a) {
	return a*a+1;
}

static PyObject* MathExt_square(PyObject *self, PyObject *args) {
    uint32_t val = 0;
    uint32_t ret = 0;
    
    if (!PyArg_ParseTuple(args, "I", &val) )
        return NULL;
    
    ret = square(val);
    
    return PyInt_FromLong(ret);
}


static PyMethodDef MathMethods[] = {
    {"square", (PyCFunction)MathExt_square, METH_VARARGS,
    "MyDemo square function"},
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC initMathExt(void)
{
    (void) Py_InitModule("MathExt", MathMethods);
}
