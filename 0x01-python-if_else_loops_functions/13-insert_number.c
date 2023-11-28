#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *ptr1 = *head, *ptr2 = ptr1->next;

	if (!*head || !head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	new->n = number;

	while (ptr1->next->n < number)
	{
		ptr1 = ptr1->next;
		ptr2 = ptr2->next;
	}

	ptr1->next = new;
	new->next = ptr2;
	return (*head);
}
