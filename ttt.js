let boxes=document.querySelectorAll(".box");
let rb=document.querySelector("#reset");
let newgamebutton=document.querySelector("newgame");
let msgcontainer=document.querySelector(".msg-container");
let msg=document.querySelector("#msg");
let turnO=true;

const resetgame=()=>{
    turnO=true;
    enableBoxes();
    msgcontainer.classList.add("hide");
};

const win=[
    [0,1,2],
    [0,4,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [2,4,6],
    [3,4,5],
    [6,7,8],
];
boxes.forEach((box)=>{
    box.addEventListener("click", () =>{
        console.log("Box was clicked!");
        if(turnO){
            box.innerText="O";
            turnO=false;
        }else{
            box.innerText="X";
            turnO=true;
        }
        checkwinner();
    });
});

const enableBoxes=()=>{
    for(let i of boxes){
        i.disabled=false;
        i.innerText="";
    }
}

const disableBoxes=()=>{
    for(let i of boxes){
        i.disabled=true;
    }
}

const showWinner =(winner)=>{
    msg.innerText= `Congratulations!! Winner is ${winner}`;
    msgcontainer.classList.remove("hide");
    disableBoxes();
};
const checkwinner =() =>{
    for(let pattern of win){
        // console.log(pattern[0],pattern[1],pattern[2]);
        let pos1val=boxes[pattern[0]].innerText;
        let pos2val=boxes[pattern[1]].innerText;
        let pos3val=boxes[pattern[2]].innerText;

        if(pos1val != "" && pos2val !="" && pos3val !=""){
            if(pos1val=== pos2val && pos2val===pos3val){
                console.log("Winner",pos1val);
                showWinner(pos1val);
            }
        }

    }
}; 

newgamebutton.addEventListener("click",resetgame);
rb.addEventListener("click",resetgame);
