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
	int *stack;

	while (lst != NULL)
	{
		len++;
		lst = lst->next;
	}
	lst = *head;
	i = 0;
	stack = malloc(sizeof(int) * (len + 1));
	if (stack == NULL)
		return (0);
	while (lst != NULL)
	{
		stack[i] = lst->n;
		if (i >= ((len / 2) + (len % 2)))
		{
			if (lst->n != stack[len - i - 1])
				return (0);
		}
		i++;
		lst = lst->next;
	}
	return (1);
}
