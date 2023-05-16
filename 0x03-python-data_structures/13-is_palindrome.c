#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the first element of the list
 * Return: 1 if it's palindrome, else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *lst = *head;
	int len = 0, i;
	int stack[1024];

	while (lst != NULL)
	{
		len++;
		lst = lst->next;
	}
	lst = *head;
	i = 0;
	while (lst != NULL)
	{
		if (i >= ((len / 2) + (len % 2)))
		{
			if (lst->n != stack[len - i - 1])
				return (0);
		}
		else
			stack[i] = lst->n;
		i++;
		lst = lst->next;
	}
	return (1);
}
