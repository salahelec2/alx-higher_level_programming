#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: A PyObject list.
 *
 * Return: nothing to return
 */
void print_python_list_info(PyObject *p)
{
    int size_of_list, alloc, i;
    PyObject *list_object;

    size_of_list = Py_SIZE(p);
    alloc = ((PyListObject *)p)->alloc;

    printf("[*] Size of the Python List = %d\n", size_of_list);
    printf("[*] Allocated = %d\n", alloc);

    for (i = 0; i < size_of_list; i++)
    {
        printf("Element %d: ", i);

        list_object = PyList_GetItem(p, i);
        printf("%s\n", Py_TYPE(list_object)->tp_name);
    }
}
