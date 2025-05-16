# BlueWindow Hosting PHP

## Project Overview

BlueWindow Hosting PHP is a multi-tenant hosting platform designed to serve multiple casino and gaming websites from a single codebase. The platform provides a flexible templating system that allows for different site designs while sharing common functionality.

## Key Features

- **Multi-tenant Architecture**: Serve multiple websites with different domains from a single codebase
- **Template System**: Flexible templating system using Blade for different site designs
- **Casino/Gaming Focus**: Specialized features for casino and gaming websites
- **Filter System**: Advanced filtering capabilities for casino listings
- **Cloud Storage Integration**: Integration with Google Cloud Storage for assets
- **Caching**: Efficient caching mechanisms for improved performance
- **Responsive Design**: Support for different devices and screen sizes

## Documentation Structure

This documentation is organized into the following sections:

1. [Installation and Setup](./installation.md) - Instructions for setting up the project
2. [Architecture Overview](./architecture.md) - High-level overview of the system architecture
3. [Core Components](./components.md) - Documentation of the main components
4. [Template System](./templates.md) - Guide to the templating system
5. [Filter System](./filters.md) - Documentation of the filtering capabilities
6. [Data Models](./data-models.md) - Information about the data models
7. [Utilities](./utilities.md) - Documentation of utility classes and functions
8. [Best Practices](./best-practices.md) - Recommended practices for development

## Quick Start

To get started with the project:

1. Ensure you have PHP 8.3 or higher installed
2. Clone the repository
3. Copy `.env.example` to `.env.local` and configure your environment variables
4. Run `composer install` to install dependencies
5. Set up the database using the provided schema
6. Configure your web server to point to the project root

See the [Installation and Setup](./installation.md) guide for detailed instructions.

## Technology Stack

- **PHP 8.3+**: Core programming language
- **BladeOne**: Templating engine
- **Illuminate/Database**: Database ORM
- **PHP-DI**: Dependency injection container
- **Google Cloud Storage**: Asset storage
- **Symfony Components**: Various utilities
- **GuzzleHTTP**: HTTP client

## License

This project is proprietary software owned by Blue Window Ltd.

## Contact

For technical support or inquiries, contact techs@bluewindowltd.com.