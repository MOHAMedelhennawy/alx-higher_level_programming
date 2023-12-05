#include "lists.h"
int is_palindrome(listint_t **head)
{
    listint_t *prev = NULL, *current = *head, *next = NULL, *ptr = *head;
    int size = 0;
    bool flag;

    /*get the size of list*/
    flag = check_size(&size, ptr);

        
    /*revers the list*/
    while (size--) {
        /*Store next*/
        next = current->next;
 
        /*Reverse current node's pointer*/
        current->next = prev;
 
        /*Move pointers one position ahead.*/
        prev = current;
        current = next;
    }
    if (flag)
        prev = prev->next;
   
    /*check if list is plindrome or not*/
    while (prev != NULL && next != NULL)
    {
        if (prev->n != next->n)
            return (0);
        prev = prev->next;
        next = next->next;
    }   
    return 1;
}

bool check_size(int *size, listint_t *ptr)
{
    while (ptr)
    {
        (*size)++;
        ptr = ptr->next;
    }

    if ((*size) % 2 != 0)
    {
        *size = (*size / 2) + 1;
        return true;
    }

    else
    {
        *size = *size / 2;
        return false;
    }
}
