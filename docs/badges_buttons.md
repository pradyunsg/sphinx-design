# Badges, Buttons & Icons {octicon}`rocket`

(badges)=

## Badges

Inline badges can be used as a labelling component.
Badges are available in each semantic color, with filled and outline variants:

- {bdg}`plain badge`
- {bdg-primary}`primary`, {bdg-primary-line}`primary-line`
- {bdg-secondary}`secondary`, {bdg-secondary-line}`secondary-line`
- {bdg-success}`success`, {bdg-success-line}`success-line`
- {bdg-info}`info`, {bdg-info-line}`info-line`
- {bdg-warning}`warning`, {bdg-warning-line}`warning-line`
- {bdg-danger}`danger`, {bdg-danger-line}`danger-line`
- {bdg-light}`light`, {bdg-light-line}`light-line`
- {bdg-dark}`dark`, {bdg-dark-line}`dark-line`

`````{dropdown} Syntax
:icon: code
:color: light

````{tab-set-code}
```{literalinclude} ./snippets/myst/badge-basic.txt
:language: markdown
```
```{literalinclude} ./snippets/rst/badge-basic.txt
:language: rst
```
````
`````

`bdg-link-` and `bdg-ref-` variants are also available for use with links and references.
The syntax is the same as for the `ref` role.

{bdg-link-primary}`https://example.com`

{bdg-link-primary-line}`explicit title <https://example.com>`

{bdg-ref-primary}`badges`

`````{dropdown} Syntax
:icon: code
:color: light

````{tab-set-code}
```{literalinclude} ./snippets/myst/badge-link.txt
:language: markdown
```
```{literalinclude} ./snippets/rst/badge-link.txt
:language: rst
```
````
`````

See [Bootstrap badges](https://getbootstrap.com/docs/5.0/components/badge/) for more information, and related [Material Design chips](https://material.io/components/chip).

(buttons)=

## Buttons

Buttons allow users to navigate to external (`button-link`) / internal (`button-ref`) links with a single tap.

```{button-link} https://example.com
```

```{button-link} https://example.com
Button text
```

```{button-link} https://example.com
:color: primary
:shadow:
```

```{button-link} https://example.com
:color: primary
:outline:
```

```{button-link} https://example.com
:color: secondary
:expand:
```

```{button-ref} buttons
:color: info
```

```{button-ref} buttons
:color: info

Reference Button text
```

`````{dropdown} Syntax
:icon: code
:color: light

````{tab-set-code}
```{literalinclude} ./snippets/myst/button-link.txt
:language: markdown
```
```{literalinclude} ./snippets/rst/button-link.txt
:language: rst
```
````
`````

Note that by default sphinx converts the content of references to raw text.
For example `**Bold text**` with `ref-type` set to `ref` will be rendered without bold:

```{button-ref} buttons
:ref-type: ref
:color: primary

**Bold text**
```

However, if using [myst-parser](https://myst-parser.readthedocs.io/), you can set the `ref-type` to `myst`, and the content will be properly rendered:

```{button-ref} buttons
:ref-type: myst
:color: primary

**Bold text**
```

Use the `click-parent` option to make the button's parent container also clickable.

:::{card} Card with an expanded button

```{button-link} https://example.com
:color: info
:expand:
:click-parent:
```

:::

See the [Material Design](https://material.io/components/buttons) and [Bootstrap](https://getbootstrap.com/docs/5.0/components/buttons/) descriptions for further details.

### `button-link` and `button-ref` options

ref-type (`button-ref` only)
: Type of reference to use; `any` (default), `ref`, `doc`, or `myst`

color
: Set the color of the button (background and font).
  One of the semantic color names: `primary`, `secondary`, `success`, `danger`, `warning`, `info`, `light`, `dark`, `muted`.

outline
: Outline color variant

align
: Align the button on the page; `left`, `right`, `center` or `justify`

expand
: Expand to fit parent width

click-parent
: Make parent container also clickable

tooltip
: Add tooltip on hover

shadow
: Add shadow CSS

class
: Additional CSS classes

(icons)=

## Inline Icons

Inline icon roles are available for both the [GitHub octicon](https://octicons-git-v2.primer.now.sh/octicons/) or [FontAwesome](https://fontawesome.com/icons?d=gallery&m=free) libraries.

Octicon icons are added as SVG's directly into the page with the `octicon` role.

By default the icon will be of height `1em` (i.e. the height of the font).
A specific height can be set after a semi-colon (`;`) with units of either `px`, `em` or `rem`.
Additional CSS classes can also be added to the SVG after a second semi-colon (`;`) delimiter.

A coloured icon: {octicon}`report;1em;sd-text-info`, some more text.

````{tab-set-code}
```{literalinclude} ./snippets/myst/icon-octicon.txt
:language: markdown
```
```{literalinclude} ./snippets/rst/icon-octicon.txt
:language: rst
```
````

````{dropdown} All Octicons
:open:

```{_all-octicon}
```
````

FontAwesome icons are added via the Fontawesome CSS classes.
If the theme you are using does not already include the FontAwesome CSS, it should be loaded in your configuration from a [font-awesome CDN](https://cdnjs.com/libraries/font-awesome), with the [html_css_files](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_css_files) option, e.g.:

```python
html_css_files = ["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/fontawesome.min.css"]
```

Use either `fa` (deprecated in font-awesome v5), `fas`, `fab` or `far` for the role name.
Note that not all regular style icons are free, `far` role only works with free ones.

````{tab-set-code}
```markdown
An icon {fas}`spinner;sd-bg-primary sd-bg-text-primary`, some more text.
```
```rst
An icon :fas:`spinner;sd-bg-primary sd-bg-text-primary`, some more text.
```
````

An icon {fas}`spinner;sd-bg-primary sd-bg-text-primary`, some more text.

By default, icons will only be output in HTML formats. But if you want fontawesome icons to be output on LaTeX, using the [fontawesome package](https://ctan.org/pkg/fontawesome), you can add to your configuration:

```python
sd_fontawesome_latex = True
```
