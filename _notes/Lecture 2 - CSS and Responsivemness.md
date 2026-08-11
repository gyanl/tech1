---
date: 11-08-2026
date modified: 08-08-2026
feed: show
key_areas:
  - "CSS — styling"
  - "Responsive web design"
  - "Hosting and deployment"
  - "Version control (Git)"
tag: lecture
title: "Lecture 2 - CSS and Responsivemness"
---

## Designing your Website

Last week we shipped a page! This week we'll figure out how to ship your page.

> **Sidenote:** Can anyone tell me why do we *ship* software?

## Steps for using Github Pages

1. Make changes.
2. Use Github to commit changes. This creates a checkpoint "locally".
3. Push to Github to push your changes online to Github.
4. Your updated website is now live at yourgithubusername.github.io

**Download Simple Web Server app**
[Download Simple Web Server](https://simplewebserver.org/)
This app is a quick and easy way to start a server on your computer, and allows you to test your website on your computer or any other device on the same wifi network - like your phone!

## CSS Properties

### Font name

The font-family property specifies the font you want to use.

```
p {
  font-family: "Roboto Condensed";
}
```

### Font Stack

If the first font in the stack is not available, the second one is used and so on. It is good practice to specify ‘serif’ or ‘sans-serif’ as a fallback in case your custom font doesn’t load.

```
body {
  font-family: Georgia, Times, "Times New Roman", serif;
}
```

### Loading fonts from Google Fonts

### Font weight

The weight of the font you want to use. Typical nomenclature is:

- 100 Thin
- 200 Extra Light
- 300 Light
- 400 Normal
- 500 Medium
- 600 Semi Bold
- 700 Bold
- 800 Extra Bold
- 900 Ultra Bold

If the font family doesn’t provide the requested weight, it will use the closest available one.

```
p {
  font-family: "Roboto Condensed";
  font-weight: 800;
}
```

### Font size

The size of the font you want to use.

```
p {
  font-family: "Roboto Condensed";
  font-size: 12px;
}
```

### Text alignment

Left, center, right or justify alignment.

```
.center{
  text-align: center;
}

.left{
  text-align: left;
}

.right{
  text-align: right;
}

.justify{
  text-align: justify;
}
```

### Text indentation

The text-indent property indents the first line of a text block.

```
p {
  text-indent: 50px;
}
```

### Tracking

The letter-spacing property controls the tracking between characters. It is convenient to use em as em is dependent on the current text size.

```
p {
  letter-spacing: 0.1em;
}
```

### Leading

The line-height property can be used to control the leading of the text. It is convenient to use em as em is dependent on the current text size.

```
p {
  line-height: 1.5em; //1.5 em is 150% of text size.
}
```

### Text Decoration

Add an underline, overline or strikethrough to text. You can specify the type and color of the line.

```
p {
  text-decoration: underline;
  text-decoration: underline overline wavy red;
}
```

### Text Transform

Capitalise first word, convert to upper or lowecase.

```
p {
  text-transform: capitalise;
  text-transform: uppercase;
  text-transform: lowercase;  
}
```

### Color

The color of the text in the block.

```
p {
  color: #ff4343;
}
```

### Background color

The background color of the block.

```
p {
  background-color: #ff4343;
}
```

## Pseudo classes

### :hover

Add this to a class and these rules will be activated only when the mouse pointer is hovering over the class.

```
p:hover {
  background-color: #ff4343;
}
```

### :first-letter

Affects only the first letter of the div.

```
p::first-letter {
  font-weight: bold;
  text-transform: uppercase;
}
```

### :first-line

Affects only the first line of the div.

```
p::first-line {
  font-weight: bold;
  text-transform: uppercase;
}
```

## Links

Links can be styled using the following properties

```
a:link { color: #666666; text-decoration: none; }
a:visited { color: #333333; }
a:hover { text-decoration: underline; }
a:active { color: #000000; }
```

### Responsive Design

### Breakpoints

