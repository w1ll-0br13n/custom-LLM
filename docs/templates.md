# Template System Documentation

This document provides a comprehensive guide to the BlueWindow Hosting PHP template system, explaining how it works and how to create or modify templates.

## Overview

The template system is a core component of the BlueWindow Hosting PHP platform, allowing different websites to have unique designs while sharing common functionality. The system uses the Blade templating engine and follows an object-oriented approach with inheritance and composition.

## Architecture

The template system consists of several key components:

1. **Base Template Class**: An abstract class that defines common functionality
2. **Template Interfaces**: Interfaces that define required methods for specific features
3. **Template Traits**: Reusable functionality shared across templates
4. **Template Implementations**: Specific implementations for different website designs
5. **Blade Templates**: HTML templates using the Blade templating engine

### Class Hierarchy

```
Template (Abstract Class)
├── Implements
│   ├── TemplateInterface
│   ├── TemplateBonusInterface
│   ├── TopsInterface
│   └── TemplateFreeGamesInterface
├── Uses
│   ├── TopsTrait
│   ├── FreeGamesTrait
│   ├── NewsTrait
│   ├── PrognosticTrait
│   ├── TemplateHelperTrait
│   └── AssetsVersioningTrait
└── Extended by
    ├── BcelTemplate
    ├── ClfTemplate
    ├── GrTemplate
    └── Other specific templates...
```

## Base Template Class

The `Template` abstract class (`app/Template/Template.php`) is the foundation of the template system. It:

- Implements several interfaces that define required functionality
- Uses traits to include shared functionality
- Defines abstract methods that must be implemented by specific templates
- Provides common methods used across all templates

Key methods in the base Template class include:

- `defaultPage()`: Renders the default page for a website
- `sitemapXml()`: Generates XML sitemaps
- `univProcess404()`: Handles 404 errors
- `currencyChange()`: Formats currency values
- `getBonusSum()`: Calculates bonus sums
- Various helper methods for rendering components

## Template Interfaces

The template system uses several interfaces to define required functionality:

- **TemplateInterface**: Core template methods
- **TemplateBonusInterface**: Methods for handling bonuses
- **TopsInterface**: Methods for handling top lists
- **TemplateFreeGamesInterface**: Methods for handling free games

These interfaces ensure that all template implementations provide the necessary functionality.

## Template Traits

Traits are used to share functionality across templates:

- **TopsTrait**: Methods for rendering top lists
- **FreeGamesTrait**: Methods for handling free games
- **NewsTrait**: Methods for handling news articles
- **PrognosticTrait**: Methods for handling prognostics
- **TemplateHelperTrait**: General helper methods
- **AssetsVersioningTrait**: Methods for asset versioning

Using traits allows for code reuse without deep inheritance hierarchies.

## Template Implementations

Each website uses a specific template implementation, which extends the base Template class and provides website-specific functionality. Template implementations are located in subdirectories of `app/Template/`, such as:

- `app/Template/Bcel/BcelTemplate.php`
- `app/Template/Clf/ClfTemplate.php`
- `app/Template/Gr/GrTemplate.php`

Each template implementation:

- Extends the base Template class
- Implements required abstract methods
- May override other methods to provide custom behavior
- May include additional methods specific to that template

## Blade Templates

The system uses the BladeOne templating engine to render HTML. Blade templates are located in the `views/` directory, with subdirectories for each template implementation:

- `views/bcel/`: Templates for the Bcel template
- `views/clf/`: Templates for the Clf template
- `views/gr/`: Templates for the Gr template

Common Blade templates are located at the root of the `views/` directory and can be used by any template implementation.

### Blade Syntax

The system uses standard Blade syntax for templates:

```blade
@extends('layout.layout')

@section('content')
    <h1>{{ $site['maintitle'] }}</h1>
    <div class="content">
        {!! $site['maintext'] !!}
    </div>
@endsection
```

## Creating a New Template

To create a new template for a website:

### 1. Create Template Class

Create a new directory in `app/Template/` for your template, e.g., `app/Template/NewTemplate/`:

```php
<?php

namespace App\Template\NewTemplate;

use App\Template\Template;

class NewTemplate extends Template
{
    public function defaultPage(): string|null
    {
        // Implementation for the default page
        return Blade::run('newtemplate.default', [
            'site' => $this->siteData->site,
            'sitedata' => $this->siteData->siteData,
            // Additional data...
        ]);
    }
    
    // Implement other required methods...
}
```

### 2. Create Blade Templates

Create a directory in `views/` for your template, e.g., `views/newtemplate/`:

```
views/newtemplate/
├── layout/
│   └── layout.blade.php
├── default.blade.php
├── casino.blade.php
└── other templates...
```

### 3. Create Layout

Create a layout template in `views/newtemplate/layout/layout.blade.php`:

```blade
<!DOCTYPE html>
<html lang="{{ $sitedata['lan'] }}">
<head>
    <meta charset="UTF-8">
    <title>{{ $site['maintitle'] }}</title>
    <!-- Include CSS and other head elements -->
</head>
<body>
    <header>
        <!-- Header content -->
    </header>
    
    <main>
        @yield('content')
    </main>
    
    <footer>
        <!-- Footer content -->
    </footer>
</body>
</html>
```

### 4. Create Page Templates

Create templates for different page types:

```blade
<!-- default.blade.php -->
@extends('newtemplate.layout.layout')

@section('content')
    <h1>{{ $site['maintitle'] }}</h1>
    <div class="content">
        {!! $site['maintext'] !!}
    </div>
@endsection
```

### 5. Register the Template

Add your template to the dependency injection container in `config/DI.php`:

```php
use App\Template\NewTemplate\NewTemplate;
use App\Template\Template;

return [
    // Other bindings...
    
    Template::class => function (ContainerInterface $c) {
        $sitedata = $c->get(SiteData::class);
        
        if ($sitedata->siteData['using_template'] === 'newtemplate') {
            return new NewTemplate($c->get(AppBootstrap::class));
        }
        
        // Other template conditions...
    },
];
```

## Modifying an Existing Template

To modify an existing template:

### 1. Override Methods

Override methods in the template class to change behavior:

```php
<?php

namespace App\Template\Bcel;

use App\Template\Template;

class BcelTemplate extends Template
{
    public function getBonusSum($r, $bonusType = 'bonus_sum'): string
    {
        // Custom implementation for this template
        // ...
    }
}
```

### 2. Modify Blade Templates

Modify the Blade templates in the corresponding directory:

```blade
<!-- views/bcel/default.blade.php -->
@extends('bcel.layout.layout')

@section('content')
    <!-- Modified content -->
@endsection
```

### 3. Add New Methods

Add new methods to the template class for template-specific functionality:

```php
<?php

namespace App\Template\Bcel;

use App\Template\Template;

class BcelTemplate extends Template
{
    public function specialFeature(): string
    {
        // Implementation of a special feature for this template
        // ...
    }
}
```

## Global Variables

The template system provides several global variables that can be used in templates:

- `$site`: Information about the current page
- `$sitedata`: Information about the current website
- `$sitelan`: The current site language
- `$pagetype`: The current page type
- `$dict`: Dictionary for translations
- `$allcbp`: List of all casinos/bookmakers

These variables are available in both PHP code and Blade templates.

## Best Practices

When working with the template system:

1. **Use Inheritance**: Extend the base Template class for new templates
2. **Use Traits**: Create traits for shared functionality
3. **Follow Naming Conventions**: Use consistent naming for methods and variables
4. **Separate Logic and Presentation**: Keep business logic in PHP classes and presentation in Blade templates
5. **Reuse Components**: Use Blade includes and components for reusable UI elements
6. **Document Your Code**: Add comments to explain complex logic
7. **Test Your Templates**: Ensure templates work correctly on different devices and browsers

## Troubleshooting

Common issues with the template system:

### Blade Template Not Found

If you get a "Template not found" error:

1. Check that the template file exists in the correct directory
2. Check that you're using the correct path in `Blade::run()`
3. Run `php vendor/bin/bladeonecli -check` to verify Blade setup

### Template Method Not Implemented

If you get a "Method not implemented" error:

1. Check that your template class implements all required methods from interfaces
2. Check that you're not calling an abstract method without implementation

### CSS/JS Not Loading

If CSS or JS files are not loading:

1. Check that the files exist in the correct location
2. Check that the paths in your templates are correct
3. Check that the asset handler in `App.php` can find the files