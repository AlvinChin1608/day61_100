# day61_100

# Learning: Integrating Bootstrap with Flask-WTF Forms in Flask Applications
In this project, I learned how to integrate Bootstrap styling into Flask-WTF forms to enhance the appearance and usability of my web application's forms. Here are some key takeaways and steps I followed:

## Key Concepts
- **Flask-WTF:** A Flask extension that simplifies working with forms and provides integration with WTForms.
- **Bootstrap:** A popular CSS framework that helps design responsive and modern web pages.
- **Jinja2 Template Inheritance:** Allows for a base template to be extended by other templates, facilitating a DRY (Don't Repeat Yourself) approach to template management.

## Benefits of Using Bootstrap with Flask-WTF

- **Responsive Design:** Bootstrap ensures that forms are mobile-friendly and adapt to different screen sizes.
- **Consistent Styling:** Provides a unified look and feel across the application, enhancing user experience.
- **Simplified Form Rendering:** Using the render_form macro simplifies form rendering, reducing boilerplate code.

### Demo
![](https://github.com/AlvinChin1608/day61_100/blob/main/gif_demo/ScreenRecording2024-07-28at20.59.00-ezgif.com-video-to-gif-converter.gif)

## Implementation Steps
1. **Setting Up Flask-WTF:**
  - Installed Flask-WTF and WTForms to handle form creation and validation in the Flask app.

2. **Creating a Form Class:**
  - Defined a form class using FlaskForm, with fields such as StringField, PasswordField, and SubmitField.
  - Used validators like DataRequired, Email, and Length to enforce input requirements.

```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = StringField(
        label='Email',
        validators=[
            DataRequired(message="Email is required."),
            Email(message="Invalid email address")
        ]
    )
    password = PasswordField(
        label='Password',
        validators=[
            DataRequired(message="Password is required."),
            Length(min=8, message="Password must be at least 8 characters long")
        ]
    )
    submit = SubmitField(label='Log in')
```
3. **Integrating Bootstrap:**
  - Utilised Bootstrap to style forms for a consistent and responsive design.
  - Used the render_form macro from bootstrap5/form.html to render the form with Bootstrap styling.

4. **Using Jinja2 Template Inheritance:**
  - Created a base.html template for the common structure, which is extended by specific page templates like login.html.
  - Implemented blocks such as {% block title %} and {% block content %} to dynamically fill content in the base layout.

5 **Rendering the Login Form with Bootstrap:**
  - Updated login.html to extend base.html and render the login form using Bootstrap styles.

