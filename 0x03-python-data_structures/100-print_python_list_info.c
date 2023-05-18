#include <Python.h>

/**
 * print_python_list_info - print information about python oobject
 * @p: python object
 * Return: Nothing (void function)
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t len;

	len = Py_ssize_t(p);
	printf("[*] Size of the Python List = %ld\n", len);
}
