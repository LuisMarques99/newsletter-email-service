const activateMoreText = () => {
    const moreTextDiv = document.querySelector('.more-text');
    if (moreTextDiv.classList.contains('active')) {
        moreTextDiv.classList.remove('active');
    } else {
        moreTextDiv.classList.add('active');
    }
}

const expandTextBehaviour = () => {
    document.querySelector('.more-btn').onclick = () => {
        activateMoreText();
    };
};

const init = () => {
    expandTextBehaviour();
};

init();