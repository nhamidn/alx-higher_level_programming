#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert node to sorted list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node;
	listint_t *tmp;
	listint_t *current;

	current = *head;
	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;
	node->next = NULL;
	if (*head == NULL)
		*head = node;
	else
	{
		while (current != NULL)
		{
			tmp = current->next;
			if (tmp == NULL)
			{
				current->next = node;
				break;
			}
			if (number >= current->n && number <= tmp->n)
			{
				current->next = node;
				node->next = tmp;
				break;
			}
			current = current->next;
		}
	}
	return (node);
}
