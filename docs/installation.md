# Installation and Setup Guide

This guide provides detailed instructions for setting up the BlueWindow Hosting PHP project in both development and production environments.

## Prerequisites

Before you begin, ensure you have the following installed:

- PHP 8.3 or higher
- Composer
- MySQL/MariaDB
- Web server (Apache or Nginx)
- Git
- Required PHP extensions:
  - json
  - gd
  - dom
  - mysqli
  - libxml
  - intl

## Development Environment Setup

### 1. Clone the Repository

```bash
git clone https://github.com/bw-gaming/bluewindow-hosting-php.git
cd bluewindow-hosting-php
```

### 2. Install Dependencies

```bash
composer install
```

### 3. Configure Environment Variables

Copy the example environment file and configure it for your environment:

```bash
cp .env.example .env.local
```

Edit `.env.local` with your specific configuration:

```
APP_ENV=development
DB_HOST=localhost
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASS=your_database_password
```

### 4. Set Up the Database

Create a database for the project and import the schema:

```bash
mysql -u your_database_user -p your_database_name < database/schema.sql
```

### 5. Configure Blade Template Engine

Run the following command to set up the Blade template engine:

```bash
php vendor/bin/bladeonecli -createfolder
```

Verify the setup:

```bash
php vendor/bin/bladeonecli -check
```

### 6. Configure Web Server

#### Apache Configuration

Create or modify your Apache virtual host configuration:

```apache
<VirtualHost *:80>
    ServerName local.example.com
    DocumentRoot /path/to/bluewindow-hosting-php
    
    <Directory /path/to/bluewindow-hosting-php>
        AllowOverride All
        Require all granted
    </Directory>
    
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

#### Nginx Configuration

```nginx
server {
    listen 80;
    server_name local.example.com;
    root /path/to/bluewindow-hosting-php;
    
    index index.php;
    
    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }
    
    location ~ \.php$ {
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_pass unix:/var/run/php/php8.3-fpm.sock;
        fastcgi_index index.php;
    }
}
```

### 7. Update Hosts File

Add the following line to your hosts file (`/etc/hosts` on Linux/Mac or `C:\Windows\System32\drivers\etc\hosts` on Windows):

```
127.0.0.1 local.example.com
```

### 8. Start the Web Server

Restart your web server to apply the configuration changes.

## Production Environment Setup

### 1. Server Requirements

- PHP 8.3 or higher
- MySQL/MariaDB
- Web server (Apache or Nginx)
- SSL certificate
- Google Cloud Storage account (for asset storage)

### 2. Deploy the Code

Clone the repository or deploy using your preferred method:

```bash
git clone https://github.com/bw-gaming/bluewindow-hosting-php.git
cd bluewindow-hosting-php
```

### 3. Install Dependencies

```bash
composer install --no-dev --optimize-autoloader
```

### 4. Configure Environment Variables

Copy the example environment file and configure it for production:

```bash
cp .env.example .env.local
```

Edit `.env.local` with your production configuration:

```
APP_ENV=production
DB_HOST=your_production_db_host
DB_NAME=your_production_db_name
DB_USER=your_production_db_user
DB_PASS=your_production_db_password
```

### 5. Set Up the Database

Import the database schema to your production database.

### 6. Configure Blade Template Engine

```bash
php vendor/bin/bladeonecli -createfolder
```

### 7. Configure Web Server

Set up your web server with proper SSL configuration and security settings.

### 8. Set Up Google Cloud Storage

Configure Google Cloud Storage for asset storage:

1. Create a Google Cloud Storage bucket
2. Set up service account credentials
3. Configure the application to use the bucket

### 9. Set Up Caching

Configure caching for improved performance:

1. Set up Redis or Memcached if needed
2. Configure the application to use the caching service

### 10. Security Considerations

- Ensure all sensitive files are protected
- Set proper file permissions
- Configure firewall rules
- Set up regular backups

## Troubleshooting

### Common Issues

#### Blade Template Engine Issues

If you encounter issues with the Blade template engine, try:

```bash
php vendor/bin/bladeonecli -check
```

#### Database Connection Issues

Verify your database credentials in the `.env.local` file.

#### Permission Issues

Ensure the web server has proper permissions to read and write to the necessary directories:

```bash
chmod -R 755 /path/to/bluewindow-hosting-php
chmod -R 777 /path/to/bluewindow-hosting-php/compiles
chmod -R 777 /path/to/bluewindow-hosting-php/cache
```

## Next Steps

After completing the installation, refer to the [Architecture Overview](./architecture.md) to understand the system structure and the [Template System](./templates.md) guide to learn how to work with templates.