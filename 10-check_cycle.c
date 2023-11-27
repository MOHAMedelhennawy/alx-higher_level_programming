#include "lists.h"
int check_cycle(listint_t *list)
{
    listint_t *fast = list->next, *slow = list;

    while (fast->next != NULL && fast != NULL)
    {
        if (list == NULL)
            return (0);

        if (slow == fast)
            return (1);

        fast = fast->next->next;
        slow = slow->next;

    }    
    return (0);
}