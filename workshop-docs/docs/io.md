# Understanding Input and Output Processing in AWS Step Functions

In AWS Step Functions, managing the flow of data between states is critical to ensure each task (or step) receives and returns the correct information. AWS provides various features to manipulate the data flow: 
- **InputPath**
- **Parameters**
- **ResultSelector**
- **ResultPath** 
- **OutputPath**

This workshop will walk you through these concepts and explain how they work in real-world scenarios.

For a more detailed guide, refer to the official AWS documentation on data flow in Step Functions: [AWS Step Functions Data Flow Simulator](https://docs.aws.amazon.com/step-functions/latest/dg/use-data-flow-simulator.html).

---

## 1. InputPath – _What_ input does a task need?

### Definition:

The **InputPath** field specifies **which part of the input** to pass to the task. If your input payload is complex or contains unnecessary information, you can use InputPath to extract only the relevant portion that the task needs.

### Example:
Consider the following input payload:

```json
{
  "customer": {
    "name": "Alice",
    "address": "123 Pizza St"
  },
  "pizzaOrder": {
    "pizzaType": "Margherita",
    "toppings": ["Mushrooms", "Olives"],
    "size": "Large"
  }
}
```

If you want to pass only the pizzaOrder section to the next state, you would use:
`"InputPath": "$.pizzaOrder"`

This results in the following input to the next task:

```json
{
  "pizzaType": "Margherita",
  "toppings": ["Mushrooms", "Olives"],
  "size": "Large"
}
```

## 2. Parameters – _How_ does the task need the structure of the input to be?

### Definition:

The Parameters field allows you to specify how the input should look before it is passed to the task. You can use this to build a custom structure for your input, combining dynamic values (from the input or workflow context) with static values.

### Example:
Let’s say you need to pass only the pizza type and size, and you want to add a static orderID field. You can define the input structure using Parameters:

```
"Parameters": {
  "PizzaType.$": "$.pizzaType",
  "Size.$": "$.size",
  "OrderID": "12345ABC"  // Static value
}
```

This transforms the input to:

```json
{
  "PizzaType": "Margherita",
  "Size": "Large",
  "OrderID": "12345ABC"
}
```

## 3. ResultSelector – _What_ to choose from the task’s output?

### Definition:

The ResultSelector field allows you to select specific values from the output of a task. You can create a new output by defining a set of key-value pairs based on the task’s result.

### Example:
If a task returns the following result after calculating the price:

```json
{
  "pizzaType": "Margherita",
  "priceDetails": {
    "basePrice": 12.00,
    "toppingsPrice": 3.00,
    "totalPrice": 15.00
  }
}
```

You can use ResultSelector to extract only the totalPrice and pizzaType:

```
"ResultSelector": {
  "TotalPrice.$": "$.priceDetails.totalPrice",
  "PizzaType.$": "$.pizzaType"
}
```

This creates the following output:

```json
{
  "TotalPrice": 15.00,
  "PizzaType": "Margherita"
}
```

## 4. ResultPath – _Where_ to put the chosen output?

### Definition:

The ResultPath field specifies where the task’s output should be placed in the original input. You can either merge the task’s output with the input or replace the input entirely.

### Example:
Consider the following input before invoking a task:

```json
{
  "customer": {
    "name": "Alice",
    "address": "123 Pizza St"
  },
  "pizzaOrder": {
    "pizzaType": "Margherita",
    "size": "Large"
  }
}
```

The task returns the following output:

```json
{
  "totalPrice": 15.00
}
```

Using ResultPath, you can merge the task result into the original input:

`"ResultPath": "$.pizzaOrder.price"`

The final output becomes:

```json
{
  "customer": {
    "name": "Alice",
    "address": "123 Pizza St"
  },
  "pizzaOrder": {
    "pizzaType": "Margherita",
    "size": "Large",
    "price": {
      "totalPrice": 15.00
    }
  }
}
```

## 5. OutputPath – _What_ output to send to the next state?

### Definition:

The OutputPath field allows you to filter the final output before passing it to the next state. This helps in removing unnecessary data and sending only the relevant information to the next state.

### Example:
Let’s say the current state produces the following output:

```json
{
  "customer": {
    "name": "Alice",
    "address": "123 Pizza St"
  },
  "pizzaOrder": {
    "pizzaType": "Margherita",
    "size": "Large",
    "price": {
      "totalPrice": 15.00
    }
  }
}
```

If you want to pass only the totalPrice to the next state, you can use:

`"OutputPath": "$.pizzaOrder.price.totalPrice"`

This results in the following output: `15.00`
