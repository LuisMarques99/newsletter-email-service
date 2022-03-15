const expandTextBehaviour = () => {
    document.getElementsByClassName('.more-btn').on('click', () => {
        this.parent().parent().find('.more-text').toggleClass('active');
    });
};

const init = () => {
    expandTextBehaviour();
};

init();