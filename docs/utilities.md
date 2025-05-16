# Utilities Documentation

This document provides a comprehensive guide to the utility classes and functions in the BlueWindow Hosting PHP platform, explaining their purpose and usage.

## Overview

The BlueWindow Hosting PHP platform includes a variety of utility classes and functions that provide common functionality used throughout the application. These utilities are organized in the `app/Utils/` directory and cover areas such as formatting, currency conversion, layout management, and more.

## Formatter Utilities

The formatter utilities are located in the `app/Utils/Formatter/` directory and provide functions for formatting various types of data.

### ImageFormatter

The `ImageFormatter` class (`app/Utils/Formatter/ImageFormatter.php`) provides utilities for handling and formatting images.

#### Key Methods

- `getImageUrl($path, $options = [])`: Generates a URL for an image with optional transformations
- `resizeImage($source, $destination, $width, $height)`: Resizes an image to the specified dimensions
- `optimizeImage($path)`: Optimizes an image for web display
- `getImageDimensions($path)`: Gets the dimensions of an image
- `getImageAlt($path, $default = '')`: Gets the alt text for an image

#### Example Usage

```php
use App\Utils\Formatter\ImageFormatter;

// Get a URL for a resized image
$imageUrl = ImageFormatter::getImageUrl('/img/casinos/casino1.jpg', [
    'width' => 200,
    'height' => 150,
    'crop' => true
]);

// Resize an image
ImageFormatter::resizeImage('/path/to/source.jpg', '/path/to/destination.jpg', 800, 600);
```

### ShortCodeFormatter

The `ShortCodeFormatter` class (`app/Utils/Formatter/ShortCodeFormatter.php`) provides utilities for handling shortcodes in content.

#### Key Methods

- `process($content)`: Processes shortcodes in content
- `addshy($text)`: Adds soft hyphens to text for better word breaking
- `formatNumber($number, $decimals = 0)`: Formats a number with the specified number of decimals
- `formatDate($date, $format = 'Y-m-d')`: Formats a date according to the specified format

#### Example Usage

```php
use App\Utils\Formatter\ShortCodeFormatter;

// Process shortcodes in content
$processedContent = ShortCodeFormatter::process($content);

// Add soft hyphens to text
$formattedText = ShortCodeFormatter::addshy('This is a long text that might need to be broken');
```

### DomFormatter

The `DomFormatter` class (`app/Utils/Formatter/DomFormatter.php`) provides utilities for manipulating DOM elements.

#### Key Methods

- `cleanHtml($html)`: Cleans HTML content
- `addTargetBlank($html)`: Adds target="_blank" to external links
- `addNofollow($html)`: Adds rel="nofollow" to specified links
- `specialConvForSitemapXml($url)`: Converts URLs for sitemap XML
- `extractFirstImage($html)`: Extracts the first image from HTML content

#### Example Usage

```php
use App\Utils\Formatter\DomFormatter;

// Clean HTML content
$cleanHtml = DomFormatter::cleanHtml($dirtyHtml);

// Add target="_blank" to external links
$htmlWithTargetBlank = DomFormatter::addTargetBlank($html);
```

## Currency Utilities

The `Currency` class (`app/Utils/Currency.php`) provides utilities for handling and converting currencies.

### Key Methods

- `currencyChange($amount, $addspace = '', $standard_currency_code = false, $onlyshortencurrency = false)`: Formats a currency amount
- `formatCurrency($amount, $options = [])`: Formats a currency amount with options
- `convertCurrency($amount, $fromCurrency, $toCurrency)`: Converts an amount from one currency to another
- `getCurrencySymbol($currencyCode)`: Gets the symbol for a currency code
- `getCurrencyName($currencyCode)`: Gets the name for a currency code

### Example Usage

```php
use App\Utils\Currency;

// Format a currency amount
$formattedAmount = Currency::currencyChange(1000, 'addspace');

// Convert a currency amount
$convertedAmount = Currency::convertCurrency(100, 'USD', 'EUR');
```

## Layout Utilities

The layout utilities are located in the `app/Utils/Layout/` directory and provide functions for managing page layouts.

### Breadcrumbs

The `Breadcrumbs` class (`app/Utils/Layout/Breadcrumbs.php`) provides utilities for generating breadcrumb navigation.

#### Key Methods

- `generate($page)`: Generates breadcrumbs for a page
- `addBreadcrumb($title, $url)`: Adds a breadcrumb to the navigation
- `getBreadcrumbs()`: Gets the current breadcrumbs
- `renderBreadcrumbs($template = 'default')`: Renders the breadcrumbs using a template

#### Example Usage

```php
use App\Utils\Layout\Breadcrumbs;

// Generate breadcrumbs for a page
$breadcrumbs = Breadcrumbs::generate($page);

// Render breadcrumbs
$breadcrumbsHtml = Breadcrumbs::renderBreadcrumbs();
```

### Header

The `Header` class (`app/Utils/Layout/Header.php`) provides utilities for managing page headers.

#### Key Methods

- `generateTitle($page)`: Generates a title for a page
- `generateMetaDescription($page)`: Generates a meta description for a page
- `generateMetaKeywords($page)`: Generates meta keywords for a page
- `generateCanonicalUrl($page)`: Generates a canonical URL for a page
- `generateHreflangTags($page)`: Generates hreflang tags for a page

#### Example Usage

```php
use App\Utils\Layout\Header;

// Generate a title for a page
$title = Header::generateTitle($page);

// Generate a meta description for a page
$metaDescription = Header::generateMetaDescription($page);
```

### Menu

The `Menu` class (`app/Utils/Layout/Menu.php`) provides utilities for generating navigation menus.

#### Key Methods

- `menuNewV1($parent, $excludedtypes = [])`: Generates a menu for a parent page
- `getMenuItems($parent)`: Gets menu items for a parent page
- `isActive($url)`: Checks if a menu item is active
- `renderMenu($items, $template = 'default')`: Renders a menu using a template

#### Example Usage

```php
use App\Utils\Layout\Menu;

// Generate a menu for a parent page
$menu = Menu::menuNewV1('main');

// Render a menu
$menuHtml = Menu::renderMenu($menuItems);
```

### ContentRole

The `ContentRole` class (`app/Utils/Layout/ContentRole.php`) provides utilities for managing content roles.

#### Key Methods

- `getContentForRole($role)`: Gets content for a specific role
- `hasRole($content, $role)`: Checks if content has a specific role
- `addRole($content, $role)`: Adds a role to content
- `removeRole($content, $role)`: Removes a role from content

#### Example Usage

```php
use App\Utils\Layout\ContentRole;

// Get content for a specific role
$content = ContentRole::getContentForRole('main');

// Check if content has a specific role
$hasRole = ContentRole::hasRole($content, 'sidebar');
```

## Dictionary Utilities

The `Dictionary` class (`app/Utils/Dictionary.php`) provides utilities for handling translations.

### Key Methods

- `get($key, $default = '')`: Gets a translation for a key
- `has($key)`: Checks if a translation exists for a key
- `set($key, $value)`: Sets a translation for a key
- `load($language)`: Loads translations for a language
- `getLanguage()`: Gets the current language

### Example Usage

```php
use App\Utils\Dictionary;

// Get a translation for a key
$translation = Dictionary::get('welcome_message', 'Welcome');

// Check if a translation exists for a key
$hasTranslation = Dictionary::has('welcome_message');
```

## AppConfig Utilities

The `AppConfig` class (`app/Utils/AppConfig.php`) provides utilities for managing application configuration.

### Key Methods

- `get($key, $default = null)`: Gets a configuration value
- `set($key, $value)`: Sets a configuration value
- `has($key)`: Checks if a configuration value exists
- `load($file)`: Loads configuration from a file
- `save()`: Saves configuration to a file

### Example Usage

```php
use App\Utils\AppConfig;

// Get a configuration value
$value = AppConfig::get('debug', false);

// Set a configuration value
AppConfig::set('debug', true);
```

## DeviceConfig Utilities

The `DeviceConfig` class (`app/Utils/DeviceConfig.php`) provides utilities for detecting and managing device information.

### Key Methods

- `isMobile()`: Checks if the current device is a mobile device
- `isTablet()`: Checks if the current device is a tablet
- `isDesktop()`: Checks if the current device is a desktop
- `getDeviceType()`: Gets the type of the current device
- `getUserAgent()`: Gets the user agent of the current device

### Example Usage

```php
use App\Utils\DeviceConfig;

// Check if the current device is a mobile device
$isMobile = DeviceConfig::isMobile();

// Get the type of the current device
$deviceType = DeviceConfig::getDeviceType();
```

## Pagination Utilities

The `Pagination` class (`app/Utils/Pagination.php`) provides utilities for handling pagination.

### Key Methods

- `paginate($items, $perPage, $page = 1)`: Paginates a collection of items
- `getPageCount($totalItems, $perPage)`: Gets the total number of pages
- `getCurrentPage()`: Gets the current page
- `getPageUrl($page)`: Gets the URL for a page
- `renderPagination($template = 'default')`: Renders pagination using a template

### Example Usage

```php
use App\Utils\Pagination;

// Paginate a collection of items
$paginatedItems = Pagination::paginate($items, 10);

// Render pagination
$paginationHtml = Pagination::renderPagination();
```

## Best Practices

When working with the utility classes:

1. **Use Static Methods**: Most utility methods are static and can be called directly on the class
2. **Cache Results**: Cache the results of expensive utility operations
3. **Handle Errors**: Handle errors and edge cases when using utility methods
4. **Follow Naming Conventions**: Follow the established naming conventions when creating new utility methods
5. **Document New Methods**: Document any new utility methods you create
6. **Test Thoroughly**: Test utility methods with various inputs and edge cases

## Extending Utilities

To extend the utility classes:

1. Create a new class in the appropriate directory (e.g., `app/Utils/Formatter/` for formatters)
2. Implement the required methods
3. Document the class and its methods
4. Test the class thoroughly

Example of extending a utility class:

```php
<?php

namespace App\Utils\Formatter;

class MyCustomFormatter
{
    public static function formatCustomData($data, $options = [])
    {
        // Implementation
    }
}
```

## Troubleshooting

### Common Issues

#### Formatting Issues

If formatting is not working as expected:

1. Check that you're using the correct formatter class and method
2. Verify that the input data is in the expected format
3. Check for any special characters or encoding issues

#### Currency Issues

If currency formatting or conversion is not working as expected:

1. Check that the currency code is valid
2. Verify that the amount is a valid number
3. Check for any locale-specific formatting issues

#### Layout Issues

If layout utilities are not working as expected:

1. Check that the page data is correctly structured
2. Verify that the template exists and is correctly formatted
3. Check for any missing or invalid parameters