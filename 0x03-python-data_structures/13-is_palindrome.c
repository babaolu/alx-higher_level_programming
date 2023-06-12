#include "lists.h"

/**
 * is_palindrome - Checks if list is palindrome
 * @head: Start of listint_t
 *
 * Return: 1 if listint_t is a palindrome,
 * 0 is if listint_t is not
 */
int is_palindrome(listint_t **head)
{
	listint_t **addlist;
	size_t len, iter;

	if (!(*head))
		return (1);
	addlist = check_cycle(*head, &len);
	if (!addlist)
		return (-1);
	for (iter = 0; iter < (len / 2); iter++)
	{
		if (addlist[iter]->n != addlist[len - iter - 1]->n)
		{
			free(addlist);
			return (0);
		}
	}
	free(addlist);
	return (1);
}

/**
 * check_cycle - Checks if list has a cycle
 * @list: head of list
 * @length: length of list
 *
 * Return: Array of pointers to the lists if not cyclic
 * NULL if cyclic
 */
void *check_cycle(listint_t *list, size_t *length)
{
	size_t len = 1024, iter = 0;
	listint_t **arr, *next;

	arr = malloc(sizeof(*arr) * len);
	if (!arr)
		return (-1);
	next = list;
	while (next)
	{
		if (iter >= (len - 1))
		{
			len *= 2;
			arr = realloc(arr, len);
			if (!arr)
				return (-1);
		}
		if (find_list(arr, next, iter))
		{
			free(arr);
			return (NULL);
		}
		arr[iter] = next;
		next = next->next;
		iter++;
	}
	*length = iter;
	return (arr);
}

/**
 * find_list - Checks if a node already exists
 * @hay_base: Array of nodes
 * @pinpoint: Node to compare array against
 * @len: Current length of array
 *
 * Return: 1 if node already exists
 * 0 if node does not yet exist
 */
int find_list(listint_t **hay_base, listint_t *pinpoint, size_t len)
{
	size_t iter;

	for (iter = 0; iter < len; iter++)
	{
		if (hay_base[iter] == pinpoint)
			return (1);
	}
	return (0);
}
