# python_django_project

## Simple "Note Taking Application"

Using Django write a note taking application.
Display a form for adding the notes on a single application page. 
Previously added notes (extracted from the database) should be placed under the form,
and ordered by the number of unique words in a text field.

### How I get it.

If we have 3 notes, for exsample:
1. To do some sports!
2. Do some do some.
3. No no nO NO No.

The length of the first one is 4 and it containes 4 unique words.

The length of the second one is also 4, but it has only 2 unique(not repeated words), 2 times 'do' and 2 times 'some',
so that counts for one plus one respectively, results two in summary.

And the last note got 5 same words, so it counts as one unique.

### Algorithm.

So the rigth order, according to my algorithm, will be: 

note3(len 5, but only 1 unique word), note2(len 4, but 2 uws), note1(length 4, and 4 unique words).

## Thats it!

Superuser: admin/admin

Database:  sqlite
