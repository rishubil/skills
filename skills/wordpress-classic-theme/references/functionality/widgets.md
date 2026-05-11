---
title: Widgets
source: https://developer.wordpress.org/themes/classic-themes/functionality/widgets/
updated: 2026-05-11
---

# Widgets

**First published:** October 22, 2014  
**Last updated:** October 29, 2022

## Overview

A widget adds content and features to a widget area, also called a sidebar. Widget areas enable site customization and can appear on single or multiple pages. Themes may contain one or many widget areas.

A widget is a PHP object that outputs some HTML. Multiple instances of the same widget type can appear on a single page. Widgets store data in the database options table and appear in the WordPress admin under **Appearance > Widgets**.

## Built-in versus stand-alone widgets

WordPress includes default widgets, with themes and plugins offering additional options. Theme widgets require the theme's activation to function. Plugin widgets remain accessible across theme changes.

## Anatomy of a Widget

Widgets visually comprise two areas:

1. Title Area
2. Widget Options

### HTML Structure

```php
<div id="text-7" class="widget widget_text">
	<div class="widget-wrap">
		<h4 class="widgettitle">
			This is a text widget
		</h4><!-- .widgettitle -->
		<div class="textwidget">
			I can put HTML in here. <a href="http://google.com/">Search me!</a>
		</div><!-- .textwidget -->
	</div><!-- .widget-wrap -->
</div><!-- #text-7 -->
```

## Developing Widgets

Creating and displaying widgets requires:

1. Extend the standard WP_Widget class and implement key functions
2. Register your widget for availability in the Widgets screen
3. Ensure your theme has at least one widget area for widget placement

### Your Widget Class

The WP_Widget class is located in wp-includes/class-wp-widget.php

```php
<?php
class My_Widget extends WP_Widget {
	public function __construct() {
		// actual widget processes
	}

	public function widget( $args, $instance ) {
		// outputs the content of the widget
	}

	public function form( $instance ) {
		// outputs the options form in the admin
	}

	public function update( $new_instance, $old_instance ) {
		// processes widget options to be saved
	}
}
```

#### Required Methods

1. **__construct**: Set up your widget with a description, name, and display width.
2. **widget()**: Process the widget options and display the HTML on your page.
3. **form()**: Display the form that will be used to set the options for your widget.
4. **update()**: Save the widget options to the database.

### Registering a Widget

```php
<?php
add_action( 'widgets_init', 'wpdocs_register_widgets' );
function wpdocs_register_widgets() {
	register_widget( 'My_Widget' );
}
```

## Sample Widget

```php
<?php
class Foo_Widget extends WP_Widget {
	public function __construct() {
		parent::__construct(
			'foo_widget', // Base ID
			'Foo_Widget', // Name
			array( 'description' => __( 'A Foo Widget', 'text_domain' ) )
		);
	}

	public function widget( $args, $instance ) {
		extract( $args );
		$title = apply_filters( 'widget_title', $instance['title'] );
		echo $before_widget;
		if ( ! empty( $title ) ) {
			echo $before_title . $title . $after_title;
		}
		echo __( 'Hello, World!', 'text_domain' );
		echo $after_widget;
	}

	public function form( $instance ) {
		if ( isset( $instance['title'] ) ) {
			$title = $instance['title'];
		} else {
			$title = __( 'New title', 'text_domain' );
		}
		?>
		<p>
			<label for="<?php echo $this->get_field_name( 'title' ); ?>"><?php _e( 'Title:' ); ?></label>
			<input class="widefat" id="<?php echo $this->get_field_id( 'title' ); ?>" name="<?php echo $this->get_field_name( 'title' ); ?>" type="text" value="<?php echo esc_attr( $title ); ?>" />
		 </p>
		<?php
	}

	public function update( $new_instance, $old_instance ) {
		$instance          = array();
		$instance['title'] = ( ! empty( $new_instance['title'] ) ) ? strip_tags( $new_instance['title'] ) : '';
		return $instance;
	}
}

// Register Foo_Widget widget
add_action( 'widgets_init', 'register_foo' );
function register_foo() {
	register_widget( 'Foo_Widget' );
}
```

## Special considerations

Widgets can be displayed programmatically in template files using `the_widget()`:

```php
<?php the_title(); ?>

<div class="content">
	<?php the_content(); ?>
</div><!-- .content -->

<div class="widget-section">
	<?php the_widget( 'My_Widget_Class' ); ?>
</div><!-- .widget-section -->
```

## Navigation

- **Previous:** [Sidebars](sidebars.md)
- **Next:** [Sticky Posts](sticky-posts.md)
