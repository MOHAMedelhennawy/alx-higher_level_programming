#include "lists.h"
#include <stdio.h>
int is_palindrome(listint_t **head)
{
    listint_t *prev = NULL, *current = *head, *next = NULL, *ptr = *head;
    int len = 0, i;

    /*get the length of list*/
    while (ptr)
    {
        len++;
        ptr = ptr->next;
    }

    i = len;
    len = len / 2;
    if (i % 2 != 0)
        len++;
        
    /*revers the list*/
    while (len--) {
        /*Store next*/
        next = current->next;
 
        /*Reverse current node's pointer*/
        current->next = prev;
 
        /*Move pointers one position ahead.*/
        prev = current;
        current = next;
    }
    if (i % 2 != 0)
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
