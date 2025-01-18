        //Show error messages incase any field(s) has error(s)
        const errorLists = document.querySelectorAll('.errorlist');

            if (errorLists.length > 0) {
                errorLists.forEach(errorList => {
                    // Add 'message' and 'is-danger' classes to the errorList element
                    errorList.classList.add('message', 'is-danger');
                    
                    // Add 'message-body' class to each child of the errorList element
                    Array.from(errorList.children).forEach(child => {
                        child.classList.add('message-body');
                    });
                });
        }