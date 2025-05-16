# Core Components Documentation

This document provides a comprehensive guide to the core components of the BlueWindow Hosting PHP platform, explaining their purpose, functionality, and how they interact.

## Overview

The BlueWindow Hosting PHP platform is built around several core components that work together to provide a flexible and powerful system for hosting multiple casino/gaming websites. These components include:

1. **App**: The main application class that handles requests
2. **AppBootstrap**: Initializes the application environment
3. **SiteData**: Manages site-specific data
4. **Template System**: Renders HTML for different websites
5. **Data Models**: Represents core entities like casinos and bonuses
6. **Filter System**: Provides filtering capabilities for casino listings
7. **Utilities**: Provides common functionality used throughout the application
8. **Blade Integration**: Integrates the Blade templating engine

## App Component

The `App` class (`app/App.php`) is the main entry point for all requests. It determines the type of request and routes it to the appropriate handler.

### Key Responsibilities

- Identifying the current website based on the domain
- Routing requests to the appropriate handler (bucket, assets, or application)
- Setting up the environment for the current website
- Handling redirects and subdomains
- Managing ETag headers for caching

### Request Handlers

The `App` class includes three main request handlers:

1. **bucketHandler**: Handles requests for assets stored in Google Cloud Storage
2. **assetsHandler**: Handles requests for static assets (CSS, JS, etc.)
3. **appHandler**: Handles application requests that require template rendering

### Example Usage

```php
// In index.php
$app = new App();
$app->handleRequest();
```

## AppBootstrap Component

The `AppBootstrap` class (`app/AppBootstrap.php`) initializes the application environment and prepares it for handling requests.

### Key Responsibilities

- Loading environment variables
- Initializing the database connection
- Setting up the dependency injection container
- Loading site-specific data
- Initializing the template system
- Setting up routes

### Route Management

The `AppBootstrap` class includes methods for defining and managing routes:

- `getRoute($template, $requestedFile)`: Gets the route handler for a requested file
- `defineRoutes()`: Defines the available routes for the application

### Example Usage

```php
// In App.php
$route = AppBootstrap::getRoute($this->website['using_template'], $this->requestedFile);
if ($route) {
    ContainerSingleton::getInstance()->get(AppBootstrap::class);
    $template = ContainerSingleton::getInstance()->get(Template::class);
    // ...
}
```

## SiteData Component

The `SiteData` class (`app/SiteData.php`) manages site-specific data, including configuration, content, and settings.

### Key Responsibilities

- Loading site data from the database
- Providing access to site-specific configuration
- Managing site content
- Handling site-specific settings

### Key Properties

- `siteData`: Contains information about the current website
- `site`: Contains information about the current page
- `mainTable`: The main database table for the current website
- `siteLan`: The language of the current website

### Example Usage

```php
// In a template class
$sitedata = $this->siteData->siteData;
$site = $this->siteData->site;
$mainTable = $this->siteData->mainTable;
$siteLan = $this->siteData->siteLan;
```

## DB Component

The `DB` class (`app/DB.php`) provides a simplified interface for database operations.

### Key Responsibilities

- Executing SQL queries
- Handling database connections
- Escaping strings for SQL queries
- Providing transaction support

### Key Methods

- `select($query)`: Executes a SELECT query and returns the results
- `insert($table, $data)`: Inserts data into a table
- `update($table, $data, $where)`: Updates data in a table
- `delete($table, $where)`: Deletes data from a table
- `escapeString($string)`: Escapes a string for use in SQL queries

### Example Usage

```php
// Execute a SELECT query
$results = DB::select("SELECT * FROM casinos WHERE casino_id = '123'");

// Insert data into a table
DB::insert('casinos', ['name' => 'Casino Name', 'url' => 'https://example.com']);

// Update data in a table
DB::update('casinos', ['name' => 'New Name'], "casino_id = '123'");

// Delete data from a table
DB::delete('casinos', "casino_id = '123'");
```

## Blade Integration

The `Blade` class (`app/Blade.php`) integrates the BladeOne templating engine with the application.

### Key Responsibilities

- Initializing the BladeOne engine
- Rendering Blade templates
- Managing template caching
- Providing access to Blade directives and functions

### Key Methods

- `run($view, $data = [])`: Renders a Blade template with the provided data
- `getEngine()`: Gets the BladeOne engine instance
- `addDirective($name, $handler)`: Adds a custom Blade directive
- `addInclude($name, $handler)`: Adds a custom Blade include

### Example Usage

```php
// Render a Blade template
$html = Blade::run('template.view', [
    'site' => $site,
    'sitedata' => $sitedata,
    'content' => $content
]);
```

## ContainerSingleton Component

The `ContainerSingleton` class (`app/ContainerSingleton.php`) provides a singleton instance of the dependency injection container.

### Key Responsibilities

- Providing a single instance of the dependency injection container
- Managing dependencies
- Resolving services

### Key Methods

- `getInstance()`: Gets the singleton instance of the container
- `get($id)`: Gets a service from the container
- `has($id)`: Checks if a service exists in the container
- `set($id, $value)`: Sets a service in the container

### Example Usage

```php
// Get the container instance
$container = ContainerSingleton::getInstance();

// Get a service from the container
$template = $container->get(Template::class);

// Check if a service exists
if ($container->has(SomeService::class)) {
    // ...
}
```

## Bucket Component

The `Bucket` class (`app/Bucket.php`) provides an interface for interacting with Google Cloud Storage.

### Key Responsibilities

- Uploading files to Google Cloud Storage
- Downloading files from Google Cloud Storage
- Getting information about files in Google Cloud Storage
- Managing file metadata

### Key Methods

- `uploadFile($source, $destination)`: Uploads a file to Google Cloud Storage
- `downloadFile($source, $destination)`: Downloads a file from Google Cloud Storage
- `downloadAsString($source)`: Downloads a file as a string
- `info($path)`: Gets information about a file
- `delete($path)`: Deletes a file

### Example Usage

```php
// Upload a file
Bucket::uploadFile('/path/to/local/file.jpg', '/path/in/bucket/file.jpg');

// Download a file
Bucket::downloadFile('/path/in/bucket/file.jpg', '/path/to/local/file.jpg');

// Get file information
$info = Bucket::info('/path/in/bucket/file.jpg');
```

## Setup Component

The `Setup` class (`app/Setup.php`) handles application setup and initialization.

### Key Responsibilities

- Setting up the application environment
- Initializing required components
- Checking system requirements
- Handling application updates

### Key Methods

- `checkRequirements()`: Checks system requirements
- `initializeComponents()`: Initializes required components
- `setupEnvironment()`: Sets up the application environment
- `handleUpdates()`: Handles application updates

### Example Usage

```php
// Check system requirements
$setup = new Setup();
$requirements = $setup->checkRequirements();
if (!$requirements['met']) {
    // Handle unmet requirements
}

// Initialize components
$setup->initializeComponents();
```

## Component Interactions

The core components interact in various ways to provide the functionality of the BlueWindow Hosting PHP platform:

1. **Request Handling**: The `App` class receives requests and routes them to the appropriate handler.
2. **Application Initialization**: The `AppBootstrap` class initializes the application environment.
3. **Template Rendering**: The `Template` system renders HTML for different websites.
4. **Data Access**: The `DB` class provides access to the database.
5. **Dependency Management**: The `ContainerSingleton` class manages dependencies.
6. **Asset Management**: The `Bucket` class manages assets in Google Cloud Storage.
7. **Site Data Management**: The `SiteData` class manages site-specific data.

## Best Practices for Working with Components

1. **Use Dependency Injection**: Use the dependency injection container to manage dependencies.
2. **Follow Single Responsibility Principle**: Each component should have a single responsibility.
3. **Use Interfaces**: Define interfaces for components to allow for easier testing and replacement.
4. **Document Component Interactions**: Document how components interact with each other.
5. **Test Components**: Write tests for components to ensure they work correctly.
6. **Handle Errors**: Handle errors and edge cases in component methods.
7. **Follow Naming Conventions**: Follow established naming conventions for components and methods.