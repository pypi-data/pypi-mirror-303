// example_module.cpp
#include <Python.h>
#include "Myexample.cpp"
 
static PyObject* py_summrize(PyObject* self, PyObject* args) {
    int a=0;
    int b=2;
    if (!PyArg_ParseTuple(args, "ii", &a,&b)) { // #解析参数格式ii=int,int
        return NULL; // 参数解析失败
    }
    summrize(a,b);
    Py_RETURN_NONE;
}
static PyObject* py_print(PyObject* self, PyObject* args) {
    const char* name;
    if (!PyArg_ParseTuple(args, "s", &name)) {
        return NULL; // 参数解析失败
    }
    printS(name);
    Py_RETURN_NONE;
}
 
static PyMethodDef ExampleMethods[] = {
    {"PySummrize", py_summrize, METH_VARARGS, "Say hello from C++"},  // python function mapping name
    {"PyPrint", py_print, METH_VARARGS, "Say hello from C++111"}, 
    {NULL, NULL, 0, NULL}
};
 
static struct PyModuleDef examplemodule = {
    PyModuleDef_HEAD_INIT,
    "Myexample", //python module name
    NULL,
    -1,
    ExampleMethods
};

PyMODINIT_FUNC PyInit_Myexample(void) {
    return PyModule_Create(&examplemodule);
}