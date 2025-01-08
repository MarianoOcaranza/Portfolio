# Personal Portfolio  

### *Technologies used*
- **Django**: Backend framework for web development (Python-based)
- **HTMX**: For integrating dynamic content updates directly in Django templates
- **SQLite3**: Default database used for develpment and testing

### *Done so far*
- Created two Django apps (`Projects` and `Pages`):
  - `Projects` app shows a list of projects created using Django admin and managed with HTMX for dynamic rendering
  - `Pages` serves static pages, such as the landing page or "About" section
    
- Created **Project** model with the following fields:
  - `title` (CharField): Name of the project
  - `preview` (ImageField): Image representing the project
  - `description` (TextField): A brief description of the project
  - `created_at` and `updated_at` (DateTimeField): Timestamps for project creation and updates

- Created view to dynamically render the list with HTMX (using hx-request header to distinguish between a full-page and fragment)
- Created view to render the landing page with normal HTML templates
- Configured URLs for routing the created views in both apps
- HTML and HTMX templates created for testing

### *What's next?*
- Start with the UI using HTML, HTMX, CSS styles and TypeScript to make it interactive
  
