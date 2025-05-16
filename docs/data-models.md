# Data Models Documentation

This document provides a comprehensive guide to the data models in the BlueWindow Hosting PHP platform, explaining the core entities and their relationships.

## Overview

The data models in BlueWindow Hosting PHP represent the core entities of the casino/gaming industry. These models are used to store and retrieve information about casinos, bonuses, payment methods, games, and software providers.

## Core Data Models

### Casino

The `Casino` class (`app/Data/Casino.php`) represents casino/gaming sites and is one of the primary entities in the system.

#### Key Properties

- `casino_id`: Unique identifier for the casino
- `name`: Name of the casino
- `url`: URL of the casino's website
- `review`: URL to the casino's review page
- `rating`: Rating of the casino
- `license`: Licensing information
- `established`: Year the casino was established
- `withdrawal_limit`: Withdrawal limit information
- `languages`: Supported languages
- `currencies`: Supported currencies

#### Key Methods

- `tops($ordertype)`: Retrieves top casinos based on the specified order type
- `univRibbon($casinoId)`: Gets ribbon information for a casino
- `validateCasino($casinoId)`: Validates a casino based on various criteria
- `getCasinoInfo($casinoId)`: Gets detailed information about a casino
- `getCasinosByFilter($filter)`: Retrieves casinos based on filter criteria

### Bonus

The `Bonus` class (`app/Data/Bonus.php`) represents bonus offers from casinos.

#### Key Properties

- `bonus_id`: Unique identifier for the bonus
- `casino_id`: ID of the casino offering the bonus
- `type`: Type of bonus (welcome, no deposit, free spins, etc.)
- `amount`: Bonus amount
- `percentage`: Bonus percentage
- `wagering`: Wagering requirements
- `code`: Bonus code (if applicable)
- `valid_until`: Expiration date

#### Key Methods

- `getBonusSum($casino, $bonusType)`: Calculates the bonus sum for a casino
- `getBonusSumNewWithExtra($casino)`: Calculates the bonus sum with extra bonuses
- `calcNoDepositBonus($subtype)`: Calculates no deposit bonuses
- `calcBonusMatch($max_bonus, $deposit4maxbonus)`: Calculates bonus match percentage
- `calculateFirstDepositBonusAndBonusMatch()`: Calculates first deposit bonus and match

### Banking

The `Banking` class (`app/Data/Banking.php`) represents payment methods supported by casinos.

#### Key Properties

- `banking_id`: Unique identifier for the payment method
- `name`: Name of the payment method
- `type`: Type of payment method (credit card, e-wallet, cryptocurrency, etc.)
- `logo`: Logo image for the payment method
- `min_deposit`: Minimum deposit amount
- `max_deposit`: Maximum deposit amount
- `deposit_time`: Typical deposit processing time
- `withdrawal_time`: Typical withdrawal processing time

#### Key Methods

- `getBankingMethods($casinoId)`: Gets payment methods supported by a casino
- `getBankingMethodDetails($bankingId)`: Gets detailed information about a payment method
- `filterCasinosByBanking($bankingId)`: Filters casinos that support a specific payment method

### FreeGame

The `FreeGame` class (`app/Data/FreeGame.php`) represents free games offered by casinos.

#### Key Properties

- `game_id`: Unique identifier for the game
- `name`: Name of the game
- `provider`: Software provider
- `type`: Game type (slot, table game, live dealer, etc.)
- `theme`: Game theme
- `features`: Game features
- `volatility`: Game volatility
- `rtp`: Return to player percentage

#### Key Methods

- `getFreeGames($casinoId)`: Gets free games offered by a casino
- `getGameDetails($gameId)`: Gets detailed information about a game
- `filterGamesByType($type)`: Filters games by type
- `filterGamesByProvider($provider)`: Filters games by software provider
- `getTopGames()`: Gets top-rated games

### Software

The `Software` class (`app/Data/Software.php`) represents gaming software providers.

#### Key Properties

- `software_id`: Unique identifier for the software provider
- `name`: Name of the software provider
- `logo`: Logo image for the software provider
- `established`: Year the provider was established
- `games_count`: Number of games in the provider's portfolio
- `popular_games`: List of popular games from the provider

#### Key Methods

- `softwareNameOfId($type)`: Gets software provider names by ID
- `getSoftwareProviders($casinoId)`: Gets software providers used by a casino
- `getSoftwareDetails($softwareId)`: Gets detailed information about a software provider
- `filterCasinosBySoftware($softwareId)`: Filters casinos that use a specific software provider

## Data Relationships

The data models in the system have various relationships:

### Casino Relationships

- **One-to-Many**: A casino can have multiple bonuses
- **Many-to-Many**: A casino can support multiple payment methods
- **Many-to-Many**: A casino can offer games from multiple software providers
- **Many-to-Many**: A casino can offer multiple free games

### Bonus Relationships

- **Many-to-One**: Multiple bonuses can belong to a single casino
- **One-to-Many**: A bonus type can have multiple bonus instances

### Banking Relationships

- **Many-to-Many**: A payment method can be supported by multiple casinos
- **One-to-Many**: A payment method type can have multiple payment methods

### FreeGame Relationships

- **Many-to-Many**: A game can be offered by multiple casinos
- **Many-to-One**: Multiple games can be provided by a single software provider
- **One-to-Many**: A game type can have multiple games

### Software Relationships

- **Many-to-Many**: A software provider can be used by multiple casinos
- **One-to-Many**: A software provider can offer multiple games

## Database Structure

The data models are stored in various database tables:

### Main Tables

- `casinos`: Stores casino information
- `bonuses`: Stores bonus information
- `banking_methods`: Stores payment method information
- `free_games`: Stores game information
- `software_providers`: Stores software provider information

### Relationship Tables

- `casino_banking`: Links casinos to payment methods
- `casino_software`: Links casinos to software providers
- `casino_games`: Links casinos to games

## Data Access

Data is accessed through static methods on the model classes. For example:

```php
// Get a casino by ID
$casino = Casino::getCasinoInfo($casinoId);

// Get bonuses for a casino
$bonuses = Bonus::getBonusesForCasino($casinoId);

// Get payment methods for a casino
$paymentMethods = Banking::getBankingMethods($casinoId);

// Get games from a software provider
$games = FreeGame::filterGamesByProvider($providerId);
```

## Data Filtering

The data models support various filtering mechanisms:

### Casino Filtering

Casinos can be filtered by:

- Country availability
- Payment methods
- Software providers
- Bonus types
- Game types
- Minimum deposit
- Rating

### Bonus Filtering

Bonuses can be filtered by:

- Type (welcome, no deposit, free spins, etc.)
- Minimum amount
- Wagering requirements
- Validity

### Game Filtering

Games can be filtered by:

- Type (slot, table game, live dealer, etc.)
- Provider
- Theme
- Features
- Volatility
- RTP

## Best Practices

When working with the data models:

1. **Use Static Methods**: Access data through the static methods provided by the model classes
2. **Cache Results**: Cache frequently accessed data to improve performance
3. **Validate Input**: Always validate input before using it in database queries
4. **Handle Relationships**: Be aware of the relationships between models when retrieving data
5. **Use Transactions**: Use database transactions for operations that modify multiple tables
6. **Document Changes**: Document any changes to the data models or database schema
7. **Test Thoroughly**: Test data access methods with various inputs and edge cases

## Example Usage

Here's an example of how to use the data models to display a list of top casinos with their bonuses:

```php
// Get top casinos
$tops = Casino::tops('best');

$html = '';
foreach ($tops['array'] as $casinoId) {
    // Get casino information
    $casino = Casino::getCasinoInfo($casinoId);
    
    // Get bonus information
    $bonusSum = Bonus::getBonusSumNewWithExtra($casino);
    
    // Get payment methods
    $paymentMethods = Banking::getBankingMethods($casinoId);
    
    // Get software providers
    $softwareProviders = Software::getSoftwareProviders($casinoId);
    
    // Build HTML
    $html .= "<div class='casino'>";
    $html .= "<h2>{$casino['name']}</h2>";
    $html .= "<p>Bonus: {$bonusSum}</p>";
    $html .= "<p>Payment Methods: " . implode(', ', array_column($paymentMethods, 'name')) . "</p>";
    $html .= "<p>Software: " . implode(', ', array_column($softwareProviders, 'name')) . "</p>";
    $html .= "</div>";
}

return $html;
```

## Troubleshooting

### Common Issues

#### Data Not Found

If data is not found:

1. Check that the ID or filter criteria are correct
2. Verify that the data exists in the database
3. Check for any filtering conditions that might exclude the data

#### Relationship Data Missing

If relationship data is missing:

1. Check that the relationship is correctly defined
2. Verify that the related data exists
3. Check for any filtering conditions that might exclude the related data

#### Performance Issues

If data retrieval is slow:

1. Consider caching frequently accessed data
2. Optimize database queries
3. Use indexes on frequently queried columns
4. Limit the amount of data retrieved at once