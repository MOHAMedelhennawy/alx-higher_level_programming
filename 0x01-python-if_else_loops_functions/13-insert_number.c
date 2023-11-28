#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *ptr1 = *head, *ptr2 = ptr1->next;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	if (ptr1->n > number)
	{
		new->next = ptr1;
		*head = new;								/*insert at beginning*/
		return (new);
	}

	while (ptr1->next->n < number && ptr2->next != NULL)
	{
		ptr1 = ptr1->next;
		ptr2 = ptr1->next;
	}

	if (ptr2->next == NULL && ptr2->n < number)
	{
		add_nodeint_end(head, number);					/*insert at end*/
		return (*head);
	}
	ptr1->next = new;
	new->next = ptr2;
	return (*head);
}
