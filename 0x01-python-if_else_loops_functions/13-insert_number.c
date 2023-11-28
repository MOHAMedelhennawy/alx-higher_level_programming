#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a node inside a sorted linked list
 * @head: the first node in the linked list
 * @number: the number to add inside the new node
 * Return: pointer to the inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *move;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new)
		new->n = number;
	else
		return (NULL);

	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	move = *head;
	while (move->next && number > move->next->n)
		move = move->next;

	new->next = move->next;
	move->next = new;
	return (new);
}