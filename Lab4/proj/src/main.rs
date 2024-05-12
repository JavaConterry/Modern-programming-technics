fn main() {
    // Your program will start here.
    println!("Hello world!");
}

#[cfg(test)]
mod tests {
    // use super::*;

    // Values Types
    fn value_add_one(mut value: i32){
        value+=1;
    }

    // fixed_size array is a reference type
    #[test]
    fn int_is_value_type(){
        let value: i32 = 5;
        value_add_one(value);
        assert_eq!(value, 6);

    }


    // Reference Types
    fn array_add_one(mut array: [i32; 5]){
        for i in 0..array.len() {
            array[i] += 1;
        }
    }

    // fixed_size array is a reference type
    #[test]
    fn fixed_array_is_value_type(){
        let array: [i32; 5] = [1, 2, 3, 4, 5];
        array_add_one(array);
    
        assert_eq!(array, [2, 3, 4, 5, 6]);

    }

}