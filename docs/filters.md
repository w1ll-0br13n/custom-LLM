# Filter System Documentation

This document provides a comprehensive guide to the BlueWindow Hosting PHP filter system, explaining how it works and how to implement filters for casino/bookmaker listings.

## Overview

The filter system allows users to filter casino and bookmaker listings based on various criteria such as bonus types, payment methods, game types, and more. The system is designed to be flexible, reusable, and easy to implement across different templates.

## Architecture

The filter system consists of several key components:

1. **ToplistFilter Class**: The core class that handles filter logic
2. **Filter Configurations**: Configuration arrays that define filter behavior
3. **Filter Functions**: Callback functions that generate filtered content
4. **Filter Layout**: HTML templates for the filter UI
5. **JavaScript**: Client-side code for handling filter interactions
6. **CSS**: Styling for the filter UI

## Filter Configuration

### Setting Up Filter Configurations

Filter configurations are defined in the template class using the `topsConfigs()` method:

```php
public function topsConfigs(): array
{
    global $site;

    return [
        'filter_name' => $site['filter'],
        'functions' => [
            'before_func' => function ($filterData, $extraData, $topListFilter) {
                return $this->beforeFilterFunction($filterData, $extraData, $topListFilter);
            },
            'top10home' => function ($filterData, $extraData, $topListFilter) {
                return $this->top10home($extraData, $filterData, $topListFilter);
            },
            'top10list' => function ($filterData, $extraData, $topListFilter) {
                return $this->getTop10List($extraData, $filterData, $topListFilter);
            },
            'all_casinos' => function ($filterData, $extraData, $topListFilter) {
                return $this->allCasinosTable($extraData, $filterData, $topListFilter);
            },
        ]
    ];
}
```

### Configuration Parameters

| Parameter             | Type     | Description                                                    |
|-----------------------|----------|----------------------------------------------------------------|
| filter_name           | string   | **Required.** The filter name for the page.                    |
| functions             | array    | **Required.** An array of functions for specific tasks.        |
| functions.before_func | callable | **Optional.** Function to process data before other functions. |
| functions.[type]      | callable | **Optional.**  Function to process tops.                       |

## Filter Functions

Filter functions are callback functions that generate the HTML content for filtered listings. Each function receives three parameters:

| Parameter      | Type         | Description                                       |
|----------------|--------------|---------------------------------------------------|
| $filterData    | array        | The data necessary to perform the filter.         |
| $extraData     | array        | Extra data specified in the configurations.       |
| $topListFilter | ToplistFilter| The `ToplistFilter` object.                       |

### Example Filter Function

```php
public static function homepageTops(array $filterData, array $extraData, ToplistFilter $topListFilter = null) 
{
    $tops = Casino::tops($filterData['ordertype']);
    $max = $tops['max'];
    $topHtml = "";
    $count = 0;
    foreach ($tops['array'] as $casinoId) {
        if ($topListFilter && !$topListFilter->validateCasino($casinoId)) {
            continue;
        }

        $topHtml .= "<div class='tops'>The top html you want to display</div>";
        $count++;
    }

    return [
        'html' => $topHtml,
        'count' => $count
    ];
}
```

### Function Return Value

Filter functions should return an array with the following structure:

```php
return [
    'html' => 'string', // The HTML content to display
    'count' => 'number' // The number of items displayed
];
```

The `before_func` function should return:

```php
return [$filterData, $extraData, $topListFilter];
```

## Using the Filter System

### Basic Usage

To use the filter system in a template:

```php
use App\Filter\ToplistFilter;

function defaultPage()
{
    list($filterTopsList, $topList) = ToplistFilter::getTopListFilter('homepageTops');

    return "{$filterTopsList['html']} 
    <div class='tops-container' id='tops__inner_{$filterTopsList['id']}' style='position: relative'>
        {$filterTopsList['divLoading']} 
        {$topList['html']}
    </div>";
}
```

### The `getTopListFilter` Method

The `getTopListFilter` method accepts the ID of the tops function defined in the filter configuration and returns:

| Key        | Type   | Description                          |
|------------|--------|--------------------------------------|
| html       | html   | The HTML for the filter layout       |
| id         | string | The unique identifier for the filter |
| divLoading | html   | The HTML for the loading circle      |

### Container Requirements

The parent container of the tops section should:

1. Have the ID returned by `getTopListFilter` preceded by `tops__inner_`
2. Have the style `position: relative` for the loading icon to display correctly

```html
<div class='tops-container' id='tops__inner_{$filterTopsList['id']}' style='position: relative'>
    {$filterTopsList['divLoading']} 
    {$topList['html']}
</div>
```

## AJAX Implementation

To handle filter interactions via AJAX, create a `toplist-filter.php` file in `/services/toplist-filter.php`:

```php
<?php

require_once dirname(__DIR__) .'/conf.php';

use App\Filter\ToplistFilter;

$filterConfigurations = require(dirname(__DIR__).'/config/filters.php');

$filterConfigurations['filter_name'] = $_POST['filter_name'];

$filterConfigurations['extra_data'] = $_POST['extra_data'];

$topsListFilter = new ToplistFilter($filterConfigurations);

$topList = $topsListFilter->getTopListViaAjax();

echo $topList['html'];
```

## Translations

The filter system requires certain translations to be defined in the `$dict` global variable:

| Key                       | Default (en)                     | 
|---------------------------|----------------------------------|
| loading                   | Loading                          | 
| (filter)best_casinos      | Best casinos                     | 
| (filter)live_casinos      | Live casino                      | 
| (filter)new_casinos       | *New casinos* or *New bookmaker* | 
| (filter)sports            | Sports                           | 
| (filter)free_spins_number | Number of free spins             | 
| (filter)free_spins        | Free spins                       | 
| (filter)exclusive_bonus   | Exclusive bonus                  | 
| (filter)filters           | Filters                          | 
| \*primary color\*         | Ex.: ```#FF5A62```               | 

## Theming

To define the color of the filters, set the `--filter-color` CSS variable in your CSS:

```css
:root {
    --filter-color: #FF5A62; /* Replace with your primary color */
}
```

## Including Required Files

### JavaScript

Include the filter JavaScript file in your template:

```html
<script src='/js/filters.js'></script>
```

### CSS

Include the filter CSS file in your template:

```html
<link rel='stylesheet' href='/css/filters.css'>
```

## Setting Default Filters

To set "No-Filter" as the default filter for all pages, use the following URL:

```
https://rbo.blue-staging.com/manage/database/migrations/update_filter_column_in_template.php?template={template}
```

Replace `{template}` with the appropriate existing template.

## Implementation Example

Here's a complete example of implementing the filter system in a template:

### Template Class

```php
<?php

namespace App\Template\Bcel;

use App\Template\Template;
use App\Filter\ToplistFilter;

class BcelTemplate extends Template
{
    public function topsConfigs(): array
    {
        global $site;

        return [
            'filter_name' => $site['filter'],
            'functions' => [
                'before_func' => function ($filterData, $extraData, $topListFilter) {
                    return $this->beforeFilterFunction($filterData, $extraData, $topListFilter);
                },
                'top10home' => function ($filterData, $extraData, $topListFilter) {
                    return $this->top10home($extraData, $filterData, $topListFilter);
                },
            ]
        ];
    }

    public function beforeFilterFunction($filterData, $extraData, $topListFilter)
    {
        // Process data before filtering
        return [$filterData, $extraData, $topListFilter];
    }

    public function top10home($extraData, $filterData, $topListFilter)
    {
        $tops = Casino::tops($filterData['ordertype']);
        $topHtml = "";
        $count = 0;
        
        foreach ($tops['array'] as $casinoId) {
            if ($topListFilter && !$topListFilter->validateCasino($casinoId)) {
                continue;
            }
            
            // Generate HTML for each casino
            $topHtml .= "<div class='tops'>Casino HTML</div>";
            $count++;
        }
        
        return [
            'html' => $topHtml,
            'count' => $count
        ];
    }

    public function defaultPage(): string
    {
        list($filterTopsList, $topList) = ToplistFilter::getTopListFilter('top10home');
        
        $content = "{$filterTopsList['html']} 
        <div class='tops-container' id='tops__inner_{$filterTopsList['id']}' style='position: relative'>
            {$filterTopsList['divLoading']} 
            {$topList['html']}
        </div>";
        
        return Blade::run('bcel.default', [
            'site' => $this->siteData->site,
            'sitedata' => $this->siteData->siteData,
            'content' => $content
        ]);
    }
}
```

### Blade Template

```blade
<!-- views/bcel/default.blade.php -->
@extends('bcel.layout.layout')

@section('content')
    <h1>{{ $site['maintitle'] }}</h1>
    
    {!! $content !!}
    
    <div class="additional-content">
        {!! $site['maintext'] !!}
    </div>
@endsection
```

## Troubleshooting

### Common Issues

#### Filters Not Displaying

If filters are not displaying:

1. Check that the filter name is correctly set in the configuration
2. Verify that the required JavaScript and CSS files are included
3. Check the browser console for JavaScript errors

#### AJAX Not Working

If AJAX filtering is not working:

1. Verify that the `toplist-filter.php` file is correctly set up
2. Check that the AJAX URL is correct
3. Check the browser console for AJAX errors

#### Styling Issues

If the filter styling is incorrect:

1. Verify that the CSS file is correctly included
2. Check that the `--filter-color` CSS variable is defined
3. Inspect the filter elements using browser developer tools

## Best Practices

When working with the filter system:

1. **Validate Casino IDs**: Always use `$topListFilter->validateCasino($casinoId)` to validate casinos
2. **Use Proper HTML Structure**: Ensure the tops container has the correct ID and styling
3. **Set Default Filters**: Configure default filters for each page type
4. **Optimize Performance**: Minimize the amount of HTML generated for each filter option
5. **Test Thoroughly**: Test filters with different combinations of options
6. **Provide Clear UI**: Make filter options clear and easy to understand for users
7. **Handle Empty Results**: Provide appropriate messaging when no results match the filter criteria