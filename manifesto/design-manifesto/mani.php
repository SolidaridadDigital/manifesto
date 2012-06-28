<script type='text/javascript' src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
<script type='text/javascript'>
	function scroll_to(section) {
		switch (section) { 
		   	case 'manifesto': 
		      	 $('html, body').animate({scrollTop:0}, 'fast');
		      	 break;
		    case 'signers': 
				     $('html, body').animate({scrollTop:740}, 'fast');
				     break; 
		   	case 'experiences': 
		      	 $('html, body').animate({scrollTop:1450}, 'fast'); 
		      	 break; 
		   	case 'about': 
		      	 $('html, body').animate({scrollTop:2500}, 'fast');
		      	 break; 
		   	default: 
		      	 $('html, body').animate({scrollTop:0}, 'fast');
		}
	}
</script>
<html>
	<head>
		<META http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<link rel="stylesheet" href="style.css" type="text/css" />
	</head>
	<body>
		<!-- begin: page -->
		<div class='page'>
			<!-- begin: header -->
			<header>
				<div id='header-wrapper' class='wrapper'>
					<a href="javascript:scroll_to('manifesto')" id='logo'> Digital solidarity</a>
					<div id='main-nav'>
						<nav>
							<ul>
								<li><a href="javascript:scroll_to('manifesto')">Manifesto</a></li>
								<li>|</li>
								<li><a href="javascript:scroll_to('experiences');">Experiences</a></li>
								<li>|</li>
								<li><a href="javascript:scroll_to('signers');" >Signers</a></li>
								<li>|</li>
								<li><a href="javascript:scroll_to('about');" >About</a></li>
							</ul>
						</nav>
					</div>		
			</header>
			<!-- end: header -->
			<div class='clear'></div>
			<!-- begin: content -->
			<div id='content' class='wrapper'>
				<section id='manifesto'>
					<div class='one-third'>
						<img src='' width='200px' height='200px'></img>
						<p>Going beyond Software Craftmanship</p>
					</div>
					<div class='two-thirds'>
							<h2 class='green text-center'>Manifesto</h2>
							<p>As digital professionals we commit to put our knowledge, 
								<br/>
								skills and experience to the service of mankind. 
								<br/>
								Through this work we want to invite to: 
							</p>
								<ul>
								<li>Go beyond well-crafted software towards software that matters</li>
								<li>Go beyond steadily adding value towards constantly making this world a better place </li>
								<li>Go beyond a community of professionals towards a global culture of digital solidarity </li>
								<li>Go beyond productive partnerships towards a fraternity that takes care of the needy </li>
							</ul>
								<p>
								That is, if the items on the left are necessary for developing useful software and creating business value, 
								we consider that the goals on the right also deserve our skills, energy and passion.</p>
								
							<div class='form-box'>
								<h3 class='light-blue'>Support</h3>
								<form>
									<ul>
										<li><label for='name'>Name</label><input type='text' /></li>
										<li><label for='email'>Email</label><input type='text' /></li>
										<li><label for='email'>Country</label><input type='text' /></li>	
										<li><input type='submit' value='Sign' class='right'/></li>
									</ul>
								</form>
							</div>
							
						</div>
					</section>
				<!-- end: manifesto -->
				<div class='divider'></div>
				<!-- begin: signers -->
				<section id='signers'>
					<div class='wrapper'>
						<h2 style='text-align:center' class='red'> Signers </h2>
						<div class='one-third'>
							<div class='center'>
								<ul class='signer-list'>
									<li><img width='80px' height='80px' />Waldo Uribe</li>
									<li><img width='80px' height='80px' />Waldo Uribe</li>
									<li><img width='80px' height='80px' />Waldo Uribe</li>
									<li><img width='80px' height='80px' />Waldo Uribe</li>
									<li><img width='80px' height='80px' />Waldo Uribe</li>
								</ul>
							</div>
						</div>
						<div class='one-third'>
							<ul class='signer-list'>
								<li><img width='80px' height='80px' />Waldo Uribe</li>
								<li><img width='80px' height='80px' />Waldo Uribe</li>
								<li><img width='80px' height='80px' />Waldo Uribe</li>
								<li><img width='80px' height='80px' />Waldo Uribe</li>
								<li><img width='80px' height='80px' />Waldo Uribe</li>
							</ul>
						</div>
						<div class='one-third'>
							<ul class='signer-list'>
								<li><img width='80px' height='80px' />Waldo Uribe</li>
								<li><img width='80px' height='80px' />Waldo Uribe</li>
								<li><img width='80px' height='80px' />Waldo Uribe</li>
								<li><img width='80px' height='80px' />Waldo Uribe</li>
								<li><a class='button' href='#'>+ More</a></li>
							</ul>
						</div>
					</div>
				</section>
				<!-- end: signers -->
				<div class='divider'></div>
				<!-- begin: experiences -->
				<section id='experiences'>
					<div class='wrapper'>
						<h2 style='text-align:center' class='teal'> Experiences </h2>
						<div class='one-third'>
							<div class='experience center'>
								<img width='200px' height='150px' />
								<p>Lorem ipsum amet bla</p>
							</div>
						</div>
						<div class='one-third'>
							<div class='experience center'>
								<img width='200px' height='150px' />
								<p>Lorem ipsum amet bla</p>
							</div>
						</div>
						<div class='one-third'>
							<div class='experience center'>
								<img width='200px' height='150px' />
								<p>Lorem ipsum amet bla</p>
							</div>
						</div>
						<div class='one-third'>
							<div class='experience center'>
								<img width='200px' height='150px' />
								<p>Lorem ipsum amet bla</p>
							</div>
						</div>
						<div class='one-third'>
							<div class='experience center'>
								<img width='200px' height='150px' />
								<p>Lorem ipsum amet bla</p>
							</div>
						</div>
						<div class='one-third'>
							<div class='experience center'>
								<a class='button'>+ More</a>
							</div>
						</div>
					</div>
				</section>
				<!-- end: experiences -->
				<div class='divider'></div>
				<!-- begin: about -->
				<section id='about'>
					<div class='wrapper'>
						<h2 style='text-align:center' class='pink'> About </h2>
						<div class='one-third'>
							<div class='experience center'>
								<img width='200px' height='150px' />
								<p>Lorem ipsum amet bla</p>
							</div>
						</div>
						<div class='one-third'>
							<div class='experience center'>
								<img width='200px' height='150px' />
								<p>Lorem ipsum amet bla</p>
							</div>
						</div>
						<div class='one-third'>
							<div class='experience center'>
								<img width='200px' height='150px' />
								<p>Lorem ipsum amet bla</p>
							</div>
						</div>
					</div>
				</section>
				<div class='divider'></div>
				<!-- end: about -->
			</div>
			<!-- end:content -->
			
			<!-- begin: footer -->
			<footer>
			
			</footer>
			<!-- end: footer -->
		</div>
		<!-- end: page -->
	</body>
</html>