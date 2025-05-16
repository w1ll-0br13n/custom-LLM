# Architecture Overview

This document provides a high-level overview of the BlueWindow Hosting PHP architecture, explaining the key components and how they interact.

## System Architecture

BlueWindow Hosting PHP is designed as a multi-tenant application that serves multiple websites from a single codebase. The architecture follows a modified MVC (Model-View-Controller) pattern with a focus on flexibility and reusability.

### High-Level Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                        Client Browser                        │
└───────────────────────────────┬─────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                         Web Server                           │
└───────────────────────────────┬─────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                        index.php                             │
└───────────────────────────────┬─────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                          App.php                             │
│                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐     │
│  │ bucketHandler│    │assetsHandler│    │ appHandler  │     │
│  └─────────────┘    └─────────────┘    └─────────────┘     │
└───────────────────────────────┬─────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                      AppBootstrap.php                        │
└───────────────────────────────┬─────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                     Template System                          │
│                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐     │
│  │ Template    │    │ Specific    │    │ Views       │     │
│  │ Base Class  │    │ Templates   │    │ (Blade)     │     │
│  └─────────────┘    └─────────────┘    └─────────────┘     │
└───────────────────────────────┬─────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                      Data Models                             │
│                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐     │
│  │ Casino      │    │ Bonus       │    │ Software    │     │
│  └─────────────┘    └─────────────┘    └─────────────┘     │
└───────────────────────────────┬─────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                      Database                                │
└─────────────────────────────────────────────────────────────┘
```

## Core Components

### 1. Request Handling

The entry point for all requests is `index.php`, which initializes the application and passes control to the `App` class. The `App` class determines the type of request and routes it to the appropriate handler:

- **bucketHandler**: Handles requests for assets stored in Google Cloud Storage
- **assetsHandler**: Handles requests for static assets (CSS, JS, etc.)
- **appHandler**: Handles application requests that require template rendering

### 2. Application Bootstrap

The `AppBootstrap` class initializes the application environment, sets up dependencies, and prepares the application for handling requests. It:

- Loads environment variables
- Initializes the database connection
- Sets up the dependency injection container
- Loads site-specific data
- Initializes the template system

### 3. Multi-tenant System

The multi-tenant system allows multiple websites to be served from a single codebase. Key components include:

- **Website Identification**: Websites are identified by their domain name or subdomain
- **Site Data**: Each website has its own configuration stored in the database
- **Template Selection**: Each website uses a specific template implementation

### 4. Template System

The template system is responsible for rendering HTML for each website. It consists of:

- **Base Template Class**: Abstract class that defines common functionality
- **Template Implementations**: Specific implementations for different website designs
- **Blade Templates**: HTML templates using the Blade templating engine
- **Template Traits**: Reusable functionality shared across templates

### 5. Data Models

Data models represent the core entities in the system:

- **Casino**: Represents casino/gaming sites
- **Bonus**: Represents bonus offers from casinos
- **Banking**: Represents payment methods
- **FreeGame**: Represents free games offered by casinos
- **Software**: Represents gaming software providers

### 6. Asset Management

Assets are managed through:

- **Google Cloud Storage**: For images and other media
- **Local Assets**: For CSS, JS, and other static files
- **Asset Versioning**: For cache busting

### 7. Caching

The system implements several caching mechanisms:

- **ETag Caching**: For browser caching of assets
- **Database Caching**: For frequently accessed data
- **Template Caching**: For compiled Blade templates

## Request Lifecycle

1. A request comes in to the web server
2. The request is routed to `index.php`
3. `App` class determines the type of request
4. The appropriate handler processes the request
5. For application requests:
   - `AppBootstrap` initializes the environment
   - The appropriate template is loaded
   - The template renders the response using Blade
   - The response is sent back to the client

## Database Structure

The database structure includes:

- **manage_websites**: Stores information about each website
- **Site-specific tables**: Each website has its own set of tables (e.g., `bcel_site`, `clf_site`)
- **Shared tables**: Some tables are shared across all websites

## Dependency Management

Dependencies are managed through:

- **Composer**: For PHP package dependencies
- **PHP-DI**: For dependency injection
- **ContainerSingleton**: For accessing the dependency container

## Security Considerations

The architecture includes several security features:

- **Input Validation**: All user input is validated and sanitized
- **Database Escaping**: SQL queries use parameterized queries or escaping
- **Content Security Policy**: For asset requests
- **SSL/TLS**: For secure communication

## Performance Optimizations

Performance is optimized through:

- **Caching**: Multiple levels of caching
- **Asset Optimization**: Minification and compression
- **Database Optimization**: Efficient queries and indexing
- **Lazy Loading**: Resources are loaded only when needed

## Extensibility

The system is designed to be extensible:

- **Template System**: New templates can be added by extending the base Template class
- **Traits**: Common functionality is shared through traits
- **Interfaces**: Key components implement interfaces for standardization