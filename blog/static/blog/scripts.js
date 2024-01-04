$(document).ready(function () {
  // Change Navbar color on scroll
  $(window).on("scroll", function () {
    if ($(window).scrollTop() > 50) {
      $(".navbar").addClass("transparent-bg");
    } else {
      $(".navbar").removeClass("transparent-bg");
    }
  });

  let isLoading = false;
  let page = 1;
  let noMoreData = false;

  $(window).scroll(function () {
    // Check if you're near the bottom of the page and there's more data to fetch
    if (
      $(window).scrollTop() + $(window).height() > $(document).height() - 100 &&
      !isLoading &&
      !noMoreData
    ) {
      isLoading = true;
      page++;

      $.getJSON("get_paginated_posts/", { page: page }, function (data) {
        if (data.length) {
          data.forEach(function (post) {
            $("#posts-container").append(`
                          <article class="media content-section">
                            <img src="${post.image}" alt="${post.author}'s Profile Image" class="mr-3" style="width:64px;height:64px;border-radius:50%;">
                            <div class="media-body">
                                <div class="article-metadata">
                                    <a class="mr-2" href="${users_profile}">${post.author}</a>
                                    <small class="text-muted">${post.date_posted}</small>
                                </div>
                                <img src="${post.image_url}" alt="Image for ${post.title}" class="img-fluid mt-3 rounded" width="400" height="20">
                                <h2><a class="article-title" href="/posts/${post.id}/">${post.title}</a></h2>
                                <p class="article-content">${post.teaser}</p>
                                <button class="teaser-button">
                                <a href="/posts/${post.id}/" class="read-more">Read More</a>
                                </button>
                            </div>
                          </article>
                        `);
          });
          isLoading = false;
        } else {
          noMoreData = true;
        }
      }).fail(function () {
        console.error("Error fetching more posts.");
        isLoading = false; // Reset flag even if there's an error
      });
    }
  });
});
