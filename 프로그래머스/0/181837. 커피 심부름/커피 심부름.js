function solution(order) {
    return order.reduce((total, menu) => {
        return menu.includes("americano") || menu === "anything" ? total + 4500 : total + 5000;
    }, 0);
}