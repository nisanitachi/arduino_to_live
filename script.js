const div=document.querySelector("#heading")
const text="aishwarya chowdhury";

function typewriter(element,text,i=0){
    
    if(i<text.length){
        element.textContent+=text[i]
        setTimeout(() => typewriter(element,text,i), 100); //to make the typewriter repeat after 50s instead of using i+1 if u use i++ after it within the loop it will be okay
        i++;

    }
    

}
typewriter(div,text,0)