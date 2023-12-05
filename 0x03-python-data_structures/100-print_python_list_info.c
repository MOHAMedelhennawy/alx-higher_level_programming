#include <Python.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size_p, allocated, idx = 0;
	PyObject *element;

	size_p = PyList_Size(p);            /*to get the size of list that *p point to*/
	allocated = ((PyListObject *)p)->allocated;
    /* (PyListObject *)p: is typecast to interpret the generic PyObject pointer p as a pointer to PyListObject */

    /*====================================*/

    /*(PyListObject *) to convert the PyObject pointer p to a pointer of type PyListObject.
     By doing this, we are telling the compiler to treat p as a pointer to a PyListObject structure.*/

    /*====================================*/

    /*->allocated: This field represents the number of elements that have been allocated in the list.
     It indicates the memory space that has been reserved for the list,
     which can be larger than the actual number of elements present in the list.*/
	printf("[*] Size of the Python List = %ld\n", size_p);
	printf("[*] Allocated = %ld\n", allocated);
	while (idx < size_p)
	{
		element = PyList_GET_ITEM(p, idx);
		printf("Element %ld: %s\n", idx, element->ob_type->tp_name);
		idx++;
	}
}