#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the first element of the list
 * Return: 1 if it's palindrome, else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *lst = *head, *tmp;
	int len = 0, i, j;

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
			tmp = *head;
			j = 0;
			while (tmp != NULL)
			{
				if (j == (len - i - 1))
				{
					if (tmp->n != lst->n)
						return (0);
				}
				j++;
				tmp = tmp->next;
			}
		}
		i++;
		lst = lst->next;
	}
	return (1);
}
