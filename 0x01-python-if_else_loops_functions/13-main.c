#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - create list and test insert in NULL / empty list
 *
 * Return: Always 0.
 */
int main(void)
{
	listint_t *head;

	head = NULL;
	print_listint(head);

	printf("-----------------\n");

	insert_node(&head, 972);

	print_listint(head);

	free_listint(head);

	return (0);
}