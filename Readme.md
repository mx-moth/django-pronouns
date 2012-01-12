django-pronouns - Correctly address your users
==============================================

Pronouns are tricky. Writing correspondence or copy with your users preferred pronoun in mind is even harder.
Wanting to break out of the gender binary damn near impossible - until now. `django-pronouns` is here to help!

When a user is signing up, they can select their preferred pronouns (usually disguised as a gender option).
The usual suspects (s/he) are there, as well as more neutral ones (they, it, xir, etc). Using them in your
copy is as simple as working out which form you need, and `django-pronouns` will do the rest. Observe:

	>>> "{{ user.pronoun.subject|title }} is awesome."
	"She is awesome"

	>>> "It is {{ user.name|pluralize }} birthday today. Go wish {{ user.pronoun.object }} happy birthday!"
	"It is Tims birthday today. Go wish him happy birthday!"

	>>> "{{ user.name }} looked at {{ user.pronoun.reflexive }} in the mirror"
	"Alex looked at himself in the mirror"

	>>> "{{ user.pronoun.possessive_determiner|title }} stuff is on the table."
	"Her stuff is on the table"

	>>> "This guitar is {{ user.pronoun.possessive_pronoun }}"
	"This guitar is hers"

If working out which form is too annoying, we can help there as well. Each of the five forms has a number of
aliases, consisting of the feminine and masculine forms joined with an underscore, as well as the (new) Spivak
forms:

* **Subject**: `he_she`, `she_he`, `ey`
* **Object**: `him_her`, `her_him`, `em`
* **Reflexive**: `himself_herself`, `herself_himself`, `emself`
* **Possessive determiner**: `his_her`, `her_his`, `eir`
* **Possessive pronoun**: `his_hers`, `hers_his`, `eirs`

Spivak was chosen as it is one of the only forms that is unambiguous across all five forms.
