fn main() {
    // Your program will start here.
    println!("Hello world!");
}

#[cfg(test)]
mod tests {

    // Value types
    fn add_one(value: i32) -> i32 {
        value+1
    }

    #[test]
    fn int_is_value_type(){
        let mut value: i32 = 5;
        value = add_one(value);
        assert_eq!(value, 6);   
    }

    // integers are still can be changed by reference
    fn value_add_one(value: &mut i32){
        *value+=1;
    }

    #[test]
    fn int_by_reference(){
        let mut value: i32 = 5;
        value_add_one(&mut value);
        assert_eq!(value, 6);   
    }


    #[test]
    fn int_variables_interaction(){
        let mut a = 1;
        let b = a;
        a += 1;
        assert_eq!(a, b+1);
    }


    // Reference Types  /  Garbage Collector
    #[test]
    fn struct_String(){
        let mut s1 = String::from("text");
        let mut s2 = s1;    // The initializing which meant to be copying the reference is named borrowing in rust.
                            // Next use of 's1' will throw an error of 'using a borrowed value' (shown in next example of ownership)
        // s1.push_str("text");
        s2.push_str("refs");
        assert_eq!("textrefs", s2.as_str()); // But we pushed different texts, hence we made a change by reference
    }

    fn add_one_no_return_ownership(mut value: i32){
        value += 1; //just goes out of scope and will be removed by distructor
    }
    fn add_one_return_ownership(mut value: i32) -> i32{
        value +1
    }

    
    // Ownership
    #[test]
    fn ownership(){
        let mut a = 1;
        add_one_no_return_ownership(a);
        assert_eq!(a, 2);
    }

    fn ret_ownership(){
        let mut a = 1;
        a = add_one_return_ownership(a);
        assert_eq!(a, 2);
    }

    #[test]
    fn distructor(){
        let mut s1 = String::from("text");
        let mut s2 = s1;                // Rust does not have a Garbage Collector, but instead it calls a Distructor function
                                        // if variable no longer keeps an object
                                        // or variable goes out of scope
        // s1.push_str("text");
        s2.push_str("refs");
        assert_eq!("textrefs", s2.as_str());
    }

    #[test]
    fn distructor_for_out_of_scope(){
        let mut a = 1;
        {
            let b = &mut a;// b goes out of scope here, so in the next step 
                           // we are able to make a new reference without of error
                           // that we use borrowed value
        }
        let c = &mut a;
        assert_eq!(*c, 1);
    }

    #[test]
    fn stack_allocation(){
        let val: i32 = 1;
        assert_eq!(val, 1)
    }

    #[test]
    fn heap_allocaton(){ //for heap allocating are used String, Vec or Box
        let heap_String_val: String = String::from("text");
        let heap_box_val: Box<i32> = Box::new(10);

        assert_eq!(heap_String_val, "text"); //String obj has str() method, thus no need in "*"
        assert_eq!(*heap_box_val, 10);
    }

}